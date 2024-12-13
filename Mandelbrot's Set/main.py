import turtle as t, numpy as np, matplotlib.pyplot as plt
import logging as lg

WHITE: tuple[int] = (1, 1, 1)
BLACK: tuple[int] = (0, 0, 0)
RED: tuple[int] = (1, 0, 0)
BLUE: tuple[int] = (0, 0, 1)
GREEN: tuple[int] = (0, 1, 0)

def map(x: int | float, oldmin: int | float, oldmax: int | float, newmin: int | float, newmax: int | float) -> float:
    return (x - oldmin) / (oldmax - oldmin) * (newmax - newmin) + newmin

def MandelbrotConverge(c: complex, x: tuple[int | float], y: tuple[int | float],
                       newx: tuple[int | float] = (-2, 2), newy: tuple[int | float] = (-2, 2),
                       *, max_iter: int = 100, power: float | int = 2, smooth: bool = False) -> int:
    c: complex = complex(map(c.real, x[0], x[1], newx[0], newx[1]),
                         map(c.imag, y[0], y[1], newy[0], newy[1]))
    z: complex = c
    # escapse_bound: float = max([abs(i) for i in newx]) ** 2 + max([abs(i) for i in newy]) ** 2
    n: int = -1
    while (n := n + 1) < max_iter:
        if abs(z) > 2:
            break
        z = z ** power + c

    if smooth:
        n = n - np.log(max(np.log(abs(z)), 1)) / np.log(power)\
            + np.log(max_iter) / np.log(power)
    return n
def JuliaConverge(z: complex, c: complex, x: tuple[int | float], y: tuple[int | float],
                  newx: tuple[int | float] = (-2, 2), newy: tuple[int | float] = (-2, 2),
                  *, max_iter: int = 100, power: float | int = 2, smooth: bool = False) -> int:
    z: complex = complex(map(z.real, x[0], x[1], newx[0], newx[1]),
                         map(z.imag, y[0], y[1], newy[0], newy[1]))
    n: int = -1
    escape_bound: float = max([abs(i) for i in newx]) ** 2 + max([abs(i) for i in newy]) ** 2
    smoothcolor: float = np.exp(-abs(z))
    while (n := n + 1) < max_iter:
        if (modulus := abs(z)) >= escape_bound:
            break
        z = z ** 2 + c
        if smooth:
            smoothcolor += np.exp(-modulus)
    
    return smoothcolor if smooth else n
def main1():
    tickrate: int | bool = False
    dot_size: int = 3
    screen_dim: tuple[int, int] = (600, 600)
    t.setup(*screen_dim)
    # t.bgcolor(*WHITE)
    t.tracer(tickrate)

    myTurtle = t.Turtle("circle", visible=False)
    myTurtle.pencolor(*WHITE)

    # Julia_Constant: complex = -0.925 + 0.19j
    for x in range( - screen_dim[0] // 2, screen_dim[0] // 2):
        myTurtle.teleport(x, -screen_dim[1] // 2)
        for y in range( - screen_dim[1] // 2, screen_dim[1] // 2):
            div_speed: int = MandelbrotConverge(complex(x, y), (- screen_dim[0] // 2, screen_dim[0] // 2),
                                                (- screen_dim[1] // 2, screen_dim[1] // 2),
                                                (-1, 1), (-0.5, 1.5))
            # div_speed: int = JuliaConverge(complex(x, y), Julia_Constant, (- screen_dim[0] // 2, screen_dim[0] // 2),
            #                               (- screen_dim[1] // 2, screen_dim[1] // 2))
            colour: float = map(100-div_speed, 0, 100, 0.4, 0.9)
            myTurtle.pencolor(*[colour * 0.5, colour * 0.7, colour])
            myTurtle.goto(x, y)

            # myTurtle.teleport(x, y)
            # myTurtle.dot(dot_size, *([1 - colour] * 3))
    
    t.tracer(True)
    t.exitonclick()

def main():
    points: int = 500
    # x_int: tuple[float] = (-1.7, 1.7)
    # y_int: tuple[float] = (-1, 1)
    x_int = (-0.75, -0.3)
    y_int = (0.4, 0.75)
    JuliasConstant: complex = -0.8 + 0.156j
    x: np.ndarray = np.linspace(*x_int, num=points)
    y: np.ndarray = np.linspace(*y_int, num=points)
    gradient: np.ndarray = np.zeros((points, points))
    for i, numx in enumerate(x):
        for j, numy in enumerate(y):
            gradient[j][i] = MandelbrotConverge(complex(numx, numy), x_int, y_int, x_int, y_int,
                                                max_iter=1000, smooth=True)
            # gradient[j][i] = JuliaConverge(complex(numx, numy), JuliasConstant, x_int, y_int, x_int, y_int,
            #                                max_iter=500, smooth=True)
    mandelbrot = plt.imshow(gradient, cmap='twilight_shifted', vmin=0, vmax=100,
                            extent=[x_int[0], x_int[1], y_int[0], y_int[1]], origin='lower')
    # plt.axis('off')
    plt.show()
    # plt.savefig("Julia's Set at -0.8 + 0.156i.png", bbox_inches='tight', pad_inches=0)
if __name__ == "__main__":
    # global logger
    # logger = lg.getLogger()
    # lg.basicConfig(filename=r".\logs\debug.log",
    #                level=lg.INFO)
    main()