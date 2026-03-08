from shapes import Point, Segment, Circle, Square


class ShapeStorage:
    def __init__(self):
        self._next_id = 1
        self._shapes = {}

    def _get_next_id(self) -> int:
        id_ = self._next_id
        self._next_id += 1
        return id_

    def add_point(self, x: float, y: float):
        id_ = self._get_next_id()
        shape = Point(id_, x, y)
        self._shapes[id_] = shape
        return shape

    def add_segment(self, x1, y1, x2, y2):
        id_ = self._get_next_id()
        shape = Segment(id_, x1, y1, x2, y2)
        self._shapes[id_] = shape
        return shape

    def add_circle(self, x, y, r):
        id_ = self._get_next_id()
        shape = Circle(id_, x, y, r)
        self._shapes[id_] = shape
        return shape

    def add_square(self, x, y, a):
        id_ = self._get_next_id()
        shape = Square(id_, x, y, a)
        self._shapes[id_] = shape
        return shape

    def delete(self, id_: int) -> bool:
        return self._shapes.pop(id_, None) is not None

    def list_all(self):
        return list(self._shapes.values())