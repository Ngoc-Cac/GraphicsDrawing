import math
import matplotlib.pyplot as plt

from tqdm import tqdm

from matplotlib.axes import Axes


_dragon_curve = {
    'F': 'F+G',
    'G': 'F-G'
}

_sierpinski = {
    'F': 'F+F−F−F+F'
}
_moving_actions = set('FG')

class L_System:
    __slots__ = '_rules'
    def __init__(self):
        self._rules = {}
        self._rules['dragon_curve'] = _dragon_curve
        self._rules['sierpinski'] = _sierpinski

    def _apply_rule(self,
        state: str,
        rule_name: str
    ):
        rule_set = self._rules[rule_name]
        return ''.join([
            rule_set[char] if char in rule_set else char
            for char in state
        ])
    def _move_turtle(self,
        start_pos: tuple[float, float],
        actions: str,
        heading: float,
        turning_angle: float = 90,
        length: float = 1
    ):
        end_pos = [*start_pos]
        for action in actions:
            if action in 'FG':
                radians = heading * math.pi / 180
                end_pos[0] += math.cos(radians) * length
                end_pos[1] += math.sin(radians) * length
            elif action == '+':
                heading += turning_angle
            elif action == '-':
                heading -= turning_angle
            else:
                raise ValueError(f'Unrecognised action {action}')
        return tuple(end_pos), heading

    def grow(self,
        inital_state: str,
        rule_name: str,
        num_iters: int = 5
    ):
        for _ in tqdm(range(num_iters)):
            inital_state = self._apply_rule(inital_state, rule_name)
        return inital_state

    def plot(self,
        state: str,
        start_pos: tuple[int, int] = (0, 0),
        heading: float = 90,
        length: float = 1,
        ax: Axes | None = None
    ):
        if ax is None:
            ax = plt.gca()

        residual_chars = ''
        xs, ys = [], []
        for char in state:
            residual_chars += char
            if char in _moving_actions:
                end_pos, heading = self._move_turtle(
                    start_pos, residual_chars,
                    heading, length=length
                )
                xs.append(start_pos[0])
                xs.append(end_pos[0])
                xs.append(None)
                ys.append(start_pos[1])
                ys.append(end_pos[1])
                ys.append(None)

                start_pos = end_pos
                residual_chars = ''

        ax.plot(xs, ys)
        return ax