from Segment import Segment
import turtle as t, time
import logging

def show(*segments: Segment) -> None:
    turtle: t.Turtle = t.Turtle("circle")
    turtle.shapesize(0.2, 0.2)
    turtle.pencolor(1, 1, 1)

    t.tracer(False)
    for segment in segments:
        turtle.teleport(segment.a[0], segment.a[1])
        turtle.goto(segment.b)
        
    t.tracer(True)

def KochCurve(*segments: Segment, depth: int = 0) -> list[Segment]:
    segs: list[Segment] = segments
    new_segs: list[Segment]
    while depth:
        new_segs = []
        for segment in segs:
            new_segs.extend(segment.KochGenerate())
        segs = new_segs
        depth -=1
    return segs

def main():
    screen_dim: tuple[int] = (800, 600)
    t.setup(*screen_dim)
    t.bgcolor('black')

    N_SIDE: int = 4
    SIDE_LENGTH: float = 400
    OFFSET: tuple[float] = (0, 150)
    INTERIOR_ANGLE: float = (180 * (N_SIDE - 2)) / N_SIDE
    # INVERT: bool = False

    vertices: list[t.Vec2D] = [t.Vec2D(OFFSET[0] - SIDE_LENGTH / 2, OFFSET[1]),
                               t.Vec2D(OFFSET[0] + SIDE_LENGTH / 2, OFFSET[1])]
    for i in range(2, N_SIDE):
        nextvertex: t.Vec2D = (vertices[i - 1] - vertices[i - 2]).rotate(INTERIOR_ANGLE - 180) + vertices[i - 1]
        vertices.append(nextvertex)
    segments: list[Segment] = [Segment(vertex, vertices[(i + 1) % len(vertices)])
                               for i, vertex in enumerate(vertices)]
    
    for i in range(5):
        t.resetscreen()
        koch_segments = KochCurve(*segments, depth = i)
        show(*koch_segments)
        time.sleep(1)

    t.mainloop()

if __name__ == "__main__":
    # global logger
    # logger = logging.getLogger(__name__)
    # logging.basicConfig(filename="Koch's main.log", level=logging.INFO)
    main()