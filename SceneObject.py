from PyQt5.Qt import QRectF, QObject, QVector2D
from PyQt5.QtGui import QBrush, QColor
import math


class SceneObject(QObject):
    frontDirection = QVector2D(0.0, 1.0)

    def __init__(self):
        super(SceneObject, self).__init__()
        self.node = None
        self.model = None

        self.drawAabb = False
        return

    def spawn(self, scene_node):
        assert self.node is None

        self.node = scene_node
        scene_node.attach_object(self)
        return

    def despawn(self):
        if self.node is not None:
            self.node.detach_object(self)
            self.node = None
        return

    def draw(self, painter):
        self.model.draw(painter, self.node.get_world_transform())
        if self.is_draw_aabb():
            painter.setBrush(QBrush(QColor(255, 255, 255)))
            painter.drawRect(self.get_world_aabb())
        return

    def set_model(self, model):
        self.model = model
        return

    def get_model(self):
        return self.model

    def get_scene_node(self):
        return self.node

    def get_aabb(self):
        return self.model.aabb

    def get_world_aabb(self):
        if self.node is None:
            return QRectF()
        else:
            return self.node.get_world_transform().mapRect(self.get_aabb())

    def set_world_position(self, pos):
        self.node.set_world_position(pos)
        return

    def move(self, pos):
        self.node.set_world_position(pos + self.node.get_world_position())
        return

    def get_world_position(self):
        return self.node.get_world_position()

    def move_local(self, move):
        # Transform 'move' to objects local coords (rotate it)
        arad = self.get_world_rotation() * math.pi / 180.0
        sina = math.sin(arad)
        cosa = math.cos(arad)
        self.move((move[0] * cosa + move[1] * sina,
                   move[1] * cosa + move[0] * sina))
        return

    def set_world_rotation(self, angle):
        self.node.set_world_rotation(angle)
        return

    def rotate(self, angle):
        self.node.set_world_rotation(self.node.get_world_rotation() + angle)
        return

    def get_world_rotation(self):
        return self.node.get_world_rotation()

    def set_world_scale(self, scale):
        self.node.set_world_scale(scale)
        return

    def scale(self, scale):
        self.node.set_world_scale(self.node.get_world_scale() * scale)
        return

    def get_world_scale(self):
        return self.node.get_world_scale()

    def get_world_direction(self):
        arad = self.get_world_rotation() * math.pi / 180.0
        return QVector2D(math.sin(arad), math.cos(arad))

    def set_world_direction(self, dir):
        arad = math.atan2(dir[0], dir[1])
        self.set_world_rotation(arad * 180.0 / math.pi)
        return

    def is_draw_aabb(self):
        return self.drawAabb

    def set_draw_aabb(self, value):
        self.drawAabb = value
        return
