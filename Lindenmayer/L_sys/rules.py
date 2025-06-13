import math

from tqdm import tqdm


class LSystem:
    rules=None
    turning_angle=90
    initial_state=None
    _moving_actions=set('FG')

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
        heading: float,
        length: float = 1
    ):
        radians = heading * math.pi / 180
        return (
            start_pos[0] + math.cos(radians) * length,
            start_pos[1] + math.sin(radians) * length,
        )

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
    def process_state(cls,
        state: str,
        start_pos: tuple[int, int] = (0, 0),
        heading: float = 90,
        length: float = 1
    ):
        stack = []
        xs, ys = [], []
        for action in state:
            if action in cls._moving_actions:
                end_pos = cls._move_turtle(start_pos, heading, length)
                xs.append(start_pos[0])
                xs.append(end_pos[0])
                xs.append(None)
                ys.append(start_pos[1])
                ys.append(end_pos[1])
                ys.append(None)

                start_pos = end_pos
            elif action == '+':
                heading += cls.turning_angle
            elif action == '-':
                heading -= cls.turning_angle
            elif action == '[':
                stack.append((start_pos, heading))
            elif action == ']':
                start_pos, heading = stack.pop()

        return xs, ys


class DragonCurve(LSystem):
    rules = {
        'F': 'F+G',
        'G': 'F-G'
    }
    turning_angle = 90
    initial_state = 'F'


class FractalPlant(LSystem):
    rules = {
        'F': 'FF',
        '_': 'F+[[_]-_]-F[-F_]+_'
    }
    turning_angle = 25
    initial_state = '-_'

class FractalBush(LSystem):
    rules = {
        'F': 'F[+FF][-FF]F[-F][+F]F'
    }
    turning_angle = 36
    initial_state = 'F'

class FractalTree(LSystem):
    rules = {
        'F': 'G[+F]-F',
        'G': 'GG'
    }
    turning_angle = 45
    initial_state = 'F'


class LevyCurve(LSystem):
    rules = {
        'F': '-F++F-'
    }
    turning_angle = 45
    initial_state = 'F++F++F++F'


class KochCurve(LSystem):
    rules = {
        'F': 'F-F++F-F'
    }
    turning_angle = 60
    initial_state = 'F'

class KochSnowflake(KochCurve):
    initial_state = 'F++F++F'


class Sierpinski(LSystem):
    rules = {
        'F': 'G-F-G',
        'G': 'F+G+F'
    }
    turning_angle = 60
    initial_state = 'F'