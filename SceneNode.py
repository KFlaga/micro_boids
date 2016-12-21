from PyQt5.QtGui import QTransform
from PyQt5.Qt import QRectF, QVector2D


class SceneNode:
    def __init__(self):
        self.worldPosition = QVector2D(0.0, 0.0)
        self.worldRotation = 0.0
        self.worldScale = QVector2D(1.0, 1.0)
        self.worldTransform = QTransform()

        self.parent = None
        self.children = []
        self.transformChanged = True

        self.attachedObject = None
        self.aabb = QRectF(0.0, 0.0, 0.0, 0.0)
        self.update_transform()
        return

    def get_world_position(self):
        return self.worldPosition

    def set_world_position(self, pos):
        self.worldPosition = pos
        self.transformChanged = True
        return

    def get_world_rotation(self):
        return self.worldRotation

    def set_world_rotation(self, angle):
        self.worldRotation = angle
        self.transformChanged = True
        return

    def get_world_scale(self):
        return self.worldScale

    def set_world_scale(self, scale):
        self.worldScale = scale
        self.transformChanged = True
        return

    def update_transform(self):
        if self.transformChanged:
            translation = QTransform()
            translation = translation.fromTranslate(self.worldPosition[0], self.worldPosition[1])
            scale = QTransform()
            scale = scale.fromScale(self.worldScale[0], self.worldScale[1])
            rot = QTransform()
            rot = rot.rotate(self.worldRotation)
            self.worldTransform = scale * rot * translation
            self.transformChanged = False
            self.update_aabb()
        return

    def get_world_transform(self) -> QTransform:
        return self.worldTransform

    def update_aabb(self):
        self.aabb = QRectF(0.0, 0.0, 0.0, 0.0)
        for child in self.children:
            self.aabb = self.aabb.united(child.aabb)
        if self.attachedObject is not None:
            self.aabb = QRectF.united(self.aabb, self.attachedObject.get_world_aabb())

        if self.parent is not None:
            self.parent.update_aabb()
        return

    def attach_child(self, child):
        assert child is not None
        assert child not in self.children

        self.children.append(child)
        child.parent = self
        return

    def detach_child(self, child):
        assert child is not None
        assert child in self.children

        self.children.remove(child)
        child.parent = None
        return

    def detach_all(self):
        for child in self.children:
            child.parent = None
        self.children = []
        return

    def change_parent(self, parent):
        if self.parent is not None:
            self.parent.detach_child(self)

        if parent is not None:
            self.parent.attach_child(self)
        else:
            self.parent = None
        return

    def attach_object(self, obj):
        assert obj is not None

        self.attachedObject = obj
        obj.node = self
        self.update_aabb()
        return

    def detach_object(self, obj):
        assert obj is not None

        self.attachedObject = None
        obj.node = None
        self.update_aabb()
        return
