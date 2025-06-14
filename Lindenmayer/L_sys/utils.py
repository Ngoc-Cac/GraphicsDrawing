import math

from PIL import Image, ImageDraw


def lines_to_image(
    xs: list[int | float],
    ys: list[int | float],
    base_resolution: int = 1024,
    pad_ratio: float | None = None,
    line_width: int = 2
) -> Image.Image:
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    xrange = (max_x - min_x)
    yrange = (max_y - min_y)

    aspect_ratio = yrange / xrange
    inner_res = (base_resolution, math.ceil(aspect_ratio * base_resolution))

    padding = 52 if pad_ratio is None else int(base_resolution * pad_ratio)
    padded_res = (inner_res[0] + padding, inner_res[1] + padding)


    image = Image.new('L', padded_res, color=255)
    drawer = ImageDraw.Draw(image)

    origin = (
        math.floor(inner_res[0] * abs(min_x / xrange)) + padding // 2,
        math.floor(inner_res[1] * abs(max_y / yrange)) + padding // 2
    )
    for i in range(0, len(xs), 2):
        drawer.line(
            (
                origin[0] + math.floor(xs[i    ] / xrange * inner_res[0]),
                origin[1] - math.floor(ys[i    ] / yrange * inner_res[1]),
                origin[0] + math.floor(xs[i + 1] / xrange * inner_res[0]),
                origin[1] - math.floor(ys[i + 1] / yrange * inner_res[1])
            ),
            fill=0, width=line_width
        )
    return image