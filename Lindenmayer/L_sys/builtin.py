from L_sys.base import LSystem


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