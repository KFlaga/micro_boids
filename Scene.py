from PyQt5.QtGui import QPainter, QBrush, QColor, QPixmap
from PyQt5.Qt import QRectF, QRect, QObject, pyqtSignal
from SceneNode import SceneNode
from SceneObject import SceneObject


class Scene(QObject):
    object_spawned = pyqtSignal(SceneObject, name='object_spawned')
    object_despawned = pyqtSignal(SceneObject, name='object_despawned')

    def __init__(self, width, height):
        super(Scene, self).__init__()
        self.rootNode = SceneNode()
        self.backgroundPixmap = None
        self.backgroundBrush = QBrush(QColor(0, 0, 0))
        self.width = width
        self.height = height
        self.sceneAabb = QRectF(0.0, 0.0, width, height)
        return

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_root_node(self):
        return self.rootNode

    def get_background_brush(self):
        return self.backgroundBrush

    def set_background_brush(self, brush):
        self.backgroundBrush = brush

    def get_background_pixmap(self):
        return self.backgroundPixmap

    def set_background_pixmap(self, pixmap):
        self.backgroundPixmap = pixmap

    def draw(self, painter):
        painter.setClipRect(self.sceneAabb)
        self.update_node(self.rootNode)
        if self.backgroundPixmap is not None:
            painter.drawPixmap(self.sceneAabb, self.backgroundPixmap, self.backgroundPixmap.rect())
        else:
            painter.fillRect(self.sceneAabb, self.backgroundBrush)

        self.draw_node(painter, self.rootNode)
        return

    def draw_node(self, painter, node):
        for childNode in node.children:
            if QRectF.intersects(self.sceneAabb, childNode.aabb):
                self.draw_node(painter, childNode)
        node.update_transform()
        if node.attachedObject is not None:
            node.attachedObject.draw(painter)
        return

    def update_node(self, node):
        for childNode in node.children:
            self.update_node(childNode)
        node.update_transform()
        return

    def spawn(self, scene_object, parent_object=None):
        node = SceneNode()
        if parent_object is None:
            self.rootNode.attach_child(node)
        else:
            parent_object.get_scene_node().attach_child(node)
        scene_object.spawn(node)

        self.object_spawned.emit(scene_object)
        return

    def despawn(self, scene_object):
        node = scene_object.get_scene_node()
        if node is not None:
            for child in node.children:
                if child.attachedObject is not None:
                    self.despawn(child.attachedObject)
            scene_object.despawn()
            node.change_parent(None)
            self.object_despawned.emit(scene_object)
        return

    def reset_scene(self):
        self.reset_node(self.rootNode)
        return

    def reset_node(self, node):
        for childNode in reversed(node.children):
            self.reset_node(childNode)
        if node.attachedObject is not None:
            self.despawn(node.attachedObject)
        return

