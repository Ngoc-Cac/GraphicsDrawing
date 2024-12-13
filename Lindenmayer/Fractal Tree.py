import turtle as t, random as rand

def fractal_tree(length: float | int, angle1: float | int, angle2: float | int, shrink: float | int, *,
                 boundary:tuple[int] | None = None, animation: bool | int = False) -> None:
    if not isinstance(boundary, tuple):
        raise TypeError("'boundary' must be a tuple of integers...")
    if not isinstance(animation, (bool, int)):
        raise TypeError("'animation' must be an integer or boolean...")
    if not isinstance(length, (int, float)):
        raise TypeError("'length' must be a float or integer...")
    if not isinstance(angle1, (int, float)):
        raise TypeError("'angle' must be a float or integer...")
    if not isinstance(angle2, (int, float)):
        raise TypeError("'angle' must be a float or integer...")
    if not isinstance(shrink, (int, float)):
        raise TypeError("'shrink' must be a float or integer...")
    elif shrink < 0 or shrink > 1:
        raise ValueError("Shrink factor must be between 0 and 1")
    if angle1 >= 360:
        angle1 = angle1 % 360
    if angle2 >= 360:
        angle2 = angle2 % 360
    
    y_coords: int
    if boundary:
        y_coords = - boundary[1] / 2 if max(angle1, angle2) < 60 or max(angle1, angle2) >= 300 else - boundary[1] / 6
    else:
        y_coords = -310 if max(angle1, angle2) < 60 or max(angle1, angle2) >= 300 else -100
    tur: t.Turtle = t.Turtle(visible=False)
    tur.pencolor(1, 1, 1)
    tur.left(90)
    tur.teleport(0, y_coords)
    tur.forward(length)
    t.tracer(animation)
    fractal_tree_recur(length, angle1, angle2, shrink, turtle=tur)
    t.tracer(True)
def fractal_tree_recur(length: float | int, angle1: float | int, angle2: float | int, shrink: float | int, turtle: t.Turtle) -> None:
    if length < 5:
        return

    orientation: float = turtle.heading()
    coords: tuple[float] = (turtle.xcor(), turtle.ycor())

    turtle.right(angle2)
    turtle.forward(length)
    fractal_tree_recur(length * shrink, angle1, angle2, shrink, turtle=turtle)

    turtle.setheading(orientation)
    turtle.teleport(coords[0], coords[1])

    turtle.left(angle1)
    turtle.forward(length)
    fractal_tree_recur(length * shrink, angle1, angle2, shrink, turtle=turtle)

def multi_branch_tree(length: float | int, shrink: float | int, specified_angles: tuple[float | int] | None = None, *,
                      boundary: tuple[float | int] | None = None, animation: int | bool = False) -> None:
    """specified angle tells the angle to turn wrt the orientation of looking in the positive y-axis
    positive angle means turning clockwise, negative angle means turning anti-clockwise
    """

    
    y_coords: float
    if boundary:
        y_coords = - boundary[1] // 2
    else:
        y_coords = -300
    turtle: t.Turtle = t.Turtle(visible=False)
    turtle.pencolor(1, 1, 1)
    turtle.setheading(90)
    turtle.teleport(0, y_coords)
    turtle.forward(length)

    t.tracer(animation)
    recur_multi_branch(length, shrink, specified_angles, turtle=turtle)
    t.tracer(True)

def recur_multi_branch(length: float | int, shrink: float | int, specified_angles: tuple[float | int], *,
                       turtle: t.Turtle) -> None:
    if length < 5:
        return
    orientation: float = turtle.heading()
    initial_pos: tuple[float] = (turtle.xcor(), turtle.ycor())
    for angle in specified_angles:
        turtle.right(angle)
        turtle.forward(length)
        recur_multi_branch(length * shrink, shrink, specified_angles, turtle=turtle)
        turtle.teleport(*initial_pos)
        turtle.setheading(orientation)
def main():
    boundary: tuple[int] = (1000, 700)
    t.setup(*boundary)
    t.bgcolor('black')

    length: float = 150
    shrink: float = 0.7
    angles: tuple[int | float] = (10, 20, -15, -30)


    # fractal_tree(length, a1, a2, shrink, boundary=boundary, animation=20)
    multi_branch_tree(length, shrink, angles, boundary=boundary, animation=0)

    t.exitonclick()

if __name__ == "__main__":
    main()