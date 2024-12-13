import turtle as t

class Segment:
    def __init__(self, start: t.Vec2D, end: t.Vec2D,) -> None:
        if not isinstance(start, t.Vec2D):
            raise TypeError("'start' must be of type t.Vec2D...")
        if not isinstance(end, t.Vec2D):
            raise TypeError("'end' must be of type t.Vec2D...")
        self.a = start
        self.b = end
    
    def KochGenerate(self) -> list['Segment']:
        new_segs: list['Segment'] = []
        b1: t.Vec2D = (self.b - self.a) * (1/3) + self.a
        a1: t.Vec2D = (self.b - b1) * (1/2) + b1
        c: t.Vec2D = (a1 - b1).rotate(60) + b1
        new_segs.extend([Segment(self.a, b1),
                         Segment(b1, c),
                         Segment(c, a1),
                         Segment(a1, self.b)])
        return new_segs