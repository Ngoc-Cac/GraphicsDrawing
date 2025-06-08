import numpy as np

from numpy.typing import NDArray


def generate_mandelbrot_set(
    c: NDArray,
    max_iter: int,
    escape_radius: int | float = 2,
    *,
    power: int | float = 2,
    smooth: bool = True,
) -> NDArray:
    z = np.array(c)
    tru_iter = -1
    gradient = np.zeros(c.shape, dtype=np.int64)
    while ((tru_iter := tru_iter + 1) < max_iter) and not np.all(mask := abs(z) > escape_radius):
        z[~mask] = z[~mask] ** power + c[~mask]
        gradient[~mask] += 1

    if smooth:
        # we only do this for the z that dont converge
        logz = np.log(abs(z))
        logz[abs(z) <= escape_radius] = 1
        gradient = gradient + 1 - np.log(logz) / np.log(2) # this is centered to the escape radius of 2
        gradient = np.clip(gradient, 0, max_iter)
    return gradient

def generate_julia_set(
    z: NDArray,
    julia_cons: complex,
    max_iter: int,
    *,
    escape_radius: int | float | None = None,
    power: float | int = 2,
    smooth: bool = True
) -> NDArray:
    if escape_radius is None:
        escape_radius = abs(z.real).max() ** 2 + abs(z.imag).max() ** 2

    z = np.array(z)
    true_iter = -1
    gradient = np.exp(-abs(z)) if smooth else np.zeros(z.shape)
    while (true_iter := true_iter + 1) < max_iter and not np.all((mask := abs(z) >= escape_radius)):
        z[~mask] = z[~mask] ** power + julia_cons

        gradient[~mask] += np.exp(-abs(z[~mask])) if smooth else 1
    
    return gradient