import threading
import time
import math
from SceneObject import SceneObject
from PyQt5.Qt import QObject, pyqtSignal, pyqtSlot, QVector2D


class PhysicsWorld(QObject):
    frameTime = 1000.0 / 30.0

    updated = pyqtSignal(name='updated')

    def __init__(self, scene):
        super(PhysicsWorld, self).__init__()
        self.scene = scene
        self.terminate = False
        self.objects = []
        self.thread = PhysicsThread(self)

        self.scene.object_spawned.connect(self.add_object)
        self.scene.object_despawned.connect(self.remove_object)

        self.collisions = []
        return

    def run(self):
        self.thread.start()
        return

    @pyqtSlot(SceneObject)
    def add_object(self, pobj):
        if isinstance(pobj, PhysicsObject):
            self.objects.append(pobj)
        return

    @pyqtSlot(SceneObject)
    def remove_object(self, pobj):
        if isinstance(pobj, PhysicsObject):
            self.objects.remove(pobj)
        return

    def update(self, ms):
        for pobj in self.objects:
            pobj.update_physics(ms)
        self.check_collisions()
        return

    def check_collisions(self):
        self.collisions = []
        for (idx1, obj1) in enumerate(self.objects):
            for (idx2, obj2) in enumerate(self.objects, idx1 + 1):
                if obj1 is not obj2:
                    self.check_collision(obj1, obj2)

        for (obj1, obj2) in self.collisions:
            obj1.on_collision(obj2)
        return

    def check_collision(self, obj1, obj2):
        if obj1.collides_with(obj2):
            self.collisions.append((obj1, obj2))
        return


class PhysicsThread(threading.Thread):
    def __init__(self, pworld):
        self.world = pworld
        threading.Thread.__init__(self)

    def run(self):
        now_time = time.time()

        while not self.world.terminate:
            last_time = now_time
            now_time = time.time()
            interval = (now_time - last_time) * 1000.0
            self.world.update(interval)

            # fire updated event
            self.world.updated.emit()

            if interval < PhysicsWorld.frameTime:
                sleepms = PhysicsWorld.frameTime - interval
                time.sleep(sleepms * 0.001)
        return


class PhysicsObject(SceneObject):
    def __init__(self):
        super(PhysicsObject, self).__init__()

        self.forces = []
        self.mass = 1
        self.accel = QVector2D(0.0, 0.0)
        self.velocity = QVector2D(0.0, 0.0)
        return

    def update_physics(self, ms):
        arad = self.get_world_rotation() * math.pi / 180.0
        sina = math.sin(arad)
        cosa = math.cos(arad)
        # compute total force and apply
        total_force_accel = QVector2D(0.0, 0.0)
        total_force_vel = QVector2D(0.0, 0.0)
        for force in self.forces:
            direction = force.direction
            if force.isDirectionLocal:
                direction = QVector2D(direction[0] * cosa - direction[1] * sina,
                                      direction[1] * cosa + direction[0] * sina)
            total_force_accel = total_force_accel + force.accelPart * direction
            total_force_vel = total_force_vel + force.velPart * direction

        vel_from_accel = self.accel
        vel_from_forces = total_force_vel / self.mass
        self.accel = total_force_accel / self.mass
        self.velocity += vel_from_accel * ms
        final_vel = self.velocity + vel_from_forces
        self.move(final_vel * ms)
        return

    def get_mass(self):
        return self.mass

    def set_mass(self, mass):
        self.mass = mass
        return

    def add_force(self, force):
        self.forces.append(force)
        return

    def remove_force(self, force):
        self.forces.remove(force)
        return

    def collides_with(self, other_object):
        if self.get_world_aabb().intersects(other_object.get_world_aabb()):
            world_path_1 = self.node.get_world_transform().map(self.model.path)
            world_path_2 = other_object.node.get_world_transform().map(other_object.model.path)
            if world_path_1.intersects(world_path_2):
                return True
        return False

    def on_collision(self, other_object):
        return


class Force:
    def __init__(self, accel=0.0, vel=0.0, dir=QVector2D(0.0, 1.0)):
        self.accelPart = accel
        self.velPart = vel
        self.direction = dir
        self.isDirectionLocal = True
        return
