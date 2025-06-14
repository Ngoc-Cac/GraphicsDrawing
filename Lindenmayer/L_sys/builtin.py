from L_sys.base import LSystem


class DragonCurve(LSystem):
    def __init__(self,
        initial_state = 'F',
        turning_angle: int | float = 90,
    ):
        rules = {
            'F': 'F+G',
            'G': 'F-G'
        }
        super().__init__(rules, initial_state, turning_angle)


class FractalPlant(LSystem):
    def __init__(self,
        initial_state = '-_',
        turning_angle: int | float = 25
    ):
        rules = {
            'F': 'FF',
            '_': 'F+[[_]-_]-F[-F_]+_'
        }
        super().__init__(rules, initial_state, turning_angle)

class FractalBush(LSystem):
    def __init__(self,
        initial_state = 'F',
        turning_angle: int | float = 36
    ):
        rules = {
            'F': 'F[+FF][-FF]F[-F][+F]F'
        }
        super().__init__(rules, initial_state, turning_angle)

class FractalTree(LSystem):
    def __init__(self,
        initial_state = 'F',
        turning_angle: int | float = 45
    ):
        rules = {
            'F': 'G[+F]-F',
            'G': 'GG'
        }
        super().__init__(rules, initial_state, turning_angle)


class LevyCurve(LSystem):
    def __init__(self,
        initial_state = 'F++F++F++F',
        turning_angle: int | float = 45
    ):
        rules = {
            'F': '-F++F-'
        }
        super().__init__(rules, initial_state, turning_angle)

class KochCurve(LSystem):
    def __init__(self,
        initial_state = 'F',
        turning_angle = 60
    ):
        rules = {
            'F': 'F-F++F-F'
        }
        super().__init__(rules, initial_state, turning_angle)

class KochSnowflake(KochCurve):
    def __init__(self,
        initial_state = 'F++F++F',
        turning_angle=60
    ):
        super().__init__(initial_state, turning_angle)


class Sierpinski(LSystem):
    def __init__(self,
        initial_state = 'F',
        turning_angle = 60
    ):
        rules = {
            'F': 'G-F-G',
            'G': 'F+G+F'
        }
        super().__init__(rules, initial_state, turning_angle)