import numpy as np

from scipy.interpolate import CubicSpline


def color_gradient(colors):
    X = [i / (len(colors) - 1) for i in range(len(colors))]
    Y = [[color[i] for color in colors] for i in range(3)]
    channels = [CubicSpline(X, y) for y in Y]
    return lambda x: [np.clip(channel(x), 0, 1) for channel in channels]