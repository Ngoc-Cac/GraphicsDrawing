import turtle as t
import logging as lg

def DragonCurve(initial: str) -> str:
    return ''.join([
        'F+F-F' if char == 'F' else char
        for char in initial
    ])

def DrawDragon(lindenmayer_str: str, turtle: t.Turtle, *, distance: float = 1) -> None:
    for char in lindenmayer_str:
        if char == "F":
            turtle.forward(distance)
        elif char == "+":
            turtle.left(120)
        else:
            turtle.right(120)

def main():
    boundary: tuple[int, int] = (1200, 600)

    t.setup(boundary[0] + 50, boundary[1] + 50)
    t.screensize(*boundary, 'black')

    myTurtle = t.Turtle(visible=False)
    myTurtle.teleport(-200, 300)
    # myTurtle.seth(90)
    myTurtle.pencolor('white')

    initial_str: str = "F"
    depth: int = 15

    for _ in range(depth):
        initial_str = DragonCurve(initial_str)

    t.tracer(0)
    DrawDragon(initial_str, myTurtle, distance=2.53)

    t.tracer(True)
    t.exitonclick()
if __name__ == '__main__':
    main()