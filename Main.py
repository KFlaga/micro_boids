import sys, random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.Qt import QVector2D

from MicroBoids import Scene, SceneFrame, InputHandler, SceneObject, Model, \
    Physics

import ui.main_window


class Main(QMainWindow, ui.main_window.Ui_MainWindow):
    globalMainInstance = None

    def __init__(self):
        super(Main, self).__init__()

        Main.globalMainInstance = self
        self.setupUi(self)

        self.scene = Scene(1000.0, 1000.0)
        self.sceneFrame = SceneFrame(self._sceneFrame, self.scene)
        self.sceneFrame.set_input(Input(self))

        self.physics = Physics.PhysicsWorld(self.scene)
        self.physics.updated.connect(self.redraw)

        self.spawnSceneEdges()

        self.center()
        self.setWindowTitle('Boids')
        self.show()
        self.physics.run()

        self.spawn_boid()
        self.spawn_boid()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def spawn_boid(self):
        w = random.randint(40, self.scene.get_width() - 40)
        h = random.randint(40, self.scene.get_height() - 40)
        r = random.randint(0, 360)
        sx = random.random() * 0.2 + 0.9
        sy = random.random() * 0.2 + 0.9

        boid = Boid(QColor(200, 100, 100))
        self.scene.spawn(boid)
        boid.set_world_position(QVector2D(w, h))
        boid.set_world_rotation(r)
        boid.set_world_scale(QVector2D(sx, sy))

        f = Physics.Force()
        f.direction = QVector2D(0.0, 1.0)
        f.isDirectionLocal = True
        f.accelPart = random.random() * 0.0001
        boid.add_force(f)
        return

    def resetScene(self):
        self.scene.reset_scene()
        return

    def closeEvent(self, event):
        self.physics.terminate = True
        super(Main, self).closeEvent(event)

    def redraw(self):
        self.sceneFrame.update()
        return

    def spawnSceneEdges(self):
        scene_edge = SceneEdgeRemover()
        self.scene.spawn(scene_edge)
        scene_edge.set_world_position(QVector2D(-500, 0))

        scene_edge = SceneEdgeRemover()
        self.scene.spawn(scene_edge)
        scene_edge.set_world_rotation(90)
        scene_edge.set_world_position(QVector2D(0, -500))

        scene_edge = SceneEdgeRemover()
        self.scene.spawn(scene_edge)
        scene_edge.set_world_rotation(90)
        scene_edge.set_world_position(QVector2D(1000, -500))

        scene_edge = SceneEdgeRemover()
        self.scene.spawn(scene_edge)
        scene_edge.set_world_position(QVector2D(-500, 1000))
        return


class Input(InputHandler):
    def __init__(self, main):
        super().__init__()
        self.main = main
        return

    def on_key_pressed(self, key):
        if key == Qt.Key_Q:
            self.main.spawn_boid()
        return


class Boid(Physics.PhysicsObject):
    def __init__(self, color):
        super(Boid, self).__init__()
        model = Model.create_triangle_model(
            (-10, -15), (0, 15), (10, -15)
        )
        model.fillColor = color
        self.set_model(model)
        return


class SceneEdgeRemover(Physics.PhysicsObject):
    def __init__(self):
        super(SceneEdgeRemover, self).__init__()
        model = Model.create_polynomial_model(
            [(-10000, -5), (10000, -5), (10000, 5), (-10000, 5)]
        )
        model.fillColor = QColor(50, 50, 50)
        self.set_model(model)
        return

    def on_collision(self, other_object):
        if isinstance(other_object, Boid):
            Main.globalMainInstance.scene.despawn(other_object)
        return


if __name__ == '__main__':
    app = QApplication([])
    game = Main()
    sys.exit(app.exec_())
