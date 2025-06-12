import math

from tqdm import tqdm


_moving_actions = set('FG')

class LSystem:
    rules=None
    turning_angle=90
    initial_state=None

    @classmethod
    def _apply_rule(cls,
        state: str
    ):
        return ''.join([
            cls.rules[char]
            if char in cls.rules else char
            for char in state
        ])
    
    @classmethod
    def _move_turtle(cls,
        start_pos: tuple[float, float],
        actions: str,
        heading: float,
        length: float = 1
    ):
        end_pos = [*start_pos]
        for action in actions:
            if action in 'FG':
                radians = heading * math.pi / 180
                end_pos[0] += math.cos(radians) * length
                end_pos[1] += math.sin(radians) * length
            elif action == '+':
                heading += cls.turning_angle
            elif action == '-':
                heading -= cls.turning_angle
            else:
                raise ValueError(f'Unrecognised action {action}')
        return tuple(end_pos), heading

    @classmethod
    def grow(cls,
        initial_state: str | None = None,
        num_iters: int = 5
    ):
        if cls.rules is None:
            raise NotImplementedError('No rules have been set')
        
        if initial_state is None:
            initial_state = cls.initial_state
        for _ in tqdm(range(num_iters)):
            initial_state = cls._apply_rule(initial_state)
        return initial_state

    @classmethod
    def plot(cls,
        state: str,
        start_pos: tuple[int, int] = (0, 0),
        heading: float = 90,
        length: float = 1
    ):

        residual_chars = ''
        xs, ys = [], []
        for char in state:
            residual_chars += char
            if char in _moving_actions:
                end_pos, heading = cls._move_turtle(
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

        return xs, ys


class DragonCurve(LSystem):
    rules = {
        'F': 'F+G',
        'G': 'F-G'
    }
    turning_angle = 90
    initial_state = 'F'

class KochCurve(LSystem):
    rules = {
        'F': 'F+F-F-F+F'
    }
    turning_angle = 90
    initial_state = 'F'

class Sierpinski(LSystem):
    rules = {
        'F': 'G-F-G',
        'G': 'F+G+F'
    }
    turning_angle = 60
    initial_state = 'F'