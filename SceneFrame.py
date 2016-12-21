from PyQt5.QtCore import Qt, QObject, QRect, QPoint
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QFrame, QWidget, QSizePolicy

from Scene import Scene
from InputHandler import InputHandler


class SceneFrame(QWidget):
    def __init__(self, frame, scene):
        super(SceneFrame, self).__init__(frame)

        self.setObjectName("sceneFrame_int")
        frame.layout().addWidget(self)
        # topLeft = frame.mapToParent(QPoint(0, 0))
        # self.viewport = QRect(topLeft.x(), topLeft.y(),
        #                      frame.width(), frame.height())
        self.frame = frame
        self.scene = scene
        self.setFocusPolicy(Qt.StrongFocus)
        self.scene.set_background_brush(QBrush(QColor(100, 100, 100)))
        self.inputHandler = InputHandler()
        self.viewport = QRect(0, 0, self.frame.width(), self.frame.height())
        return

    def get_scene(self):
        return self.scene

    def get_root_node(self):
        return self.scene.get_root_node()

    def get_input(self):
        return self.inputHandler

    def set_input(self, inputHandler):
        self.inputHandler = inputHandler

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setViewport(self.viewport)
        painter.setWindow(QRect(0, 0, self.scene.get_width(), self.scene.get_height()))
        painter.setViewTransformEnabled(True)
        self.scene.draw(painter)
        return

    def keyPressEvent(self, event):
        super(SceneFrame, self).keyPressEvent(event)
        key = event.key()
        self.inputHandler.on_key_pressed(key)

    def keyReleaseEvent(self, event):
        super(SceneFrame, self).keyPressEvent(event)
        key = event.key()
        self.inputHandler.on_key_released(key)

    def resizeEvent(self, event):
        # topLeft = self.frame.mapToParent(QPoint(0, 0))
        self.viewport = QRect(0, 0, self.frame.width(), self.frame.height())
        return
