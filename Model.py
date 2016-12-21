from PyQt5.QtGui import QPainter, QColor, QPainterPath, QBrush, QPen
from PyQt5.Qt import QRectF


class Model:
    def __init__(self):
        super().__init__()
        self.borderThickness = 0
        self.borderColor = QColor()
        self.fillColor = QColor()
        self.path = QPainterPath()
        self.aabb = QRectF()
        return

    def draw(self, painter, transform):
        painter.save()
        painter.setTransform(transform, True)

        painter.setBrush(QBrush(self.fillColor))
        painter.setPen(QPen(self.borderColor, self.borderThickness))
        painter.drawPath(self.path)

        painter.restore()
        return

    @classmethod
    def create_triangle_model(cls, v1, v2, v3):
        model = cls()
        model.path.moveTo(v1[0], v1[1])
        model.path.lineTo(v2[0], v2[1])
        model.path.lineTo(v3[0], v3[1])
        model.path.closeSubpath()

        left = min(v1[0], v2[0], v3[0])
        right = max(v1[0], v2[0], v3[0])
        top = min(v1[1], v2[1], v3[1])
        bot = max(v1[1], v2[1], v3[1])

        model.aabb = QRectF(left, top, right - left, bot - top)

        return model

    @classmethod
    def create_polynomial_model(cls, vs):
        model = cls()
        model.path.moveTo(vs[len(vs)-1][0], vs[len(vs)-1][1])
        for v in vs:
            model.path.lineTo(v[0], v[1])
        model.path.closeSubpath()

        left = 10000
        right = -10000
        top = 10000
        bot = -10000
        for v in vs:
            left = min(left, v[0])
            right = max(right, v[0])
            top = min(top, v[1])
            bot = max(bot, v[1])

        model.aabb = QRectF(left, top, right - left, bot - top)

        return model


    # @classmethod
    # def create_polygon_model(cls, vs):
    #     model = cls()
    #     for v in vs:
    #         model.path.moveTo(v[0], v[1])
    #     model.path.closeSubpath()
    #     return model


