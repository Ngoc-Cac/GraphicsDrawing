import math

from tqdm import tqdm


def _move_turtle(
    start_pos: tuple[float, float],
    heading: float,
    length: float = 1
):
    radians = math.radians(heading)
    return (
        round(start_pos[0] + math.cos(radians) * length, 10),
        round(start_pos[1] + math.sin(radians) * length, 10),
    )

class LSystem:
    __slots__='_rules', '_initial_state', '_turning_angle', '_shrink_factor'
    _moving_actions=set('FG')

    def __init__(self,
        rules: dict[str, str] | None = None,
        initial_state: str | None = None,
        turning_angle: int | float = 90,
        shrink_factor: int | float = 1,
    ):
        if not isinstance(rules, dict):
            raise TypeError('rules must be a dict')
        if not isinstance(initial_state, str):
            raise TypeError('inital_state must be a string')
        
        self._rules = rules
        self._initial_state = initial_state
        self.turning_angle = turning_angle
        self.shrink_factor = shrink_factor

    @property
    def rules(self) -> dict[str, str]:
        return dict(self._rules)
    @property
    def initial_state(self) -> str:
        return self._initial_state
    
    @property
    def turning_angle(self) -> int | float:
        return self._turning_angle
    @turning_angle.setter
    def turning_angle(self, angle: int | float):
        if not isinstance(angle, int | float):
            raise TypeError('turning_angle must be a number in degrees')
        self._turning_angle = angle

    @property
    def shrink_factor(self) -> int | float:
        return self._shrink_factor
    @shrink_factor.setter
    def shrink_factor(self, shrink_factor: int | float):
        if not isinstance(shrink_factor, int | float):
            raise TypeError('shrink_factor must be a positive number')
        elif shrink_factor <= 0:
            raise ValueError('shrink_factor must be a positive number')
        self._shrink_factor = shrink_factor


    def _apply_rule(self, state: str):
        return ''.join([
            self.rules[char]
            if char in self.rules else char
            for char in state
        ])


    def grow(self,
        initial_state: str | None = None,
        num_iters: int = 5
    ):
        if self.rules is None:
            raise NotImplementedError('No rules have been set')
        
        if initial_state is None:
            initial_state = self.initial_state
        for _ in tqdm(range(num_iters)):
            initial_state = self._apply_rule(initial_state)
        return initial_state

    def process_state(self,
        state: str,
        start_pos: tuple[int, int] = (0, 0),
        heading: float = 90,
        length: float = 1
    ):
        stack = []
        xs, ys = [], []
        for action in state:
            if action in self._moving_actions:
                end_pos = _move_turtle(start_pos, heading, length)
                xs.append(start_pos[0])
                xs.append(end_pos[0])
                xs.append(None)
                ys.append(start_pos[1])
                ys.append(end_pos[1])
                ys.append(None)

                start_pos = end_pos
            elif action == '+': heading += self.turning_angle
            elif action == '-': heading -= self.turning_angle
            elif action == '*': length  *= self.shrink_factor
            elif action == '/': length  /= self.shrink_factor
            elif action == '[':
                stack.append((start_pos, heading))
            elif action == ']':
                start_pos, heading = stack.pop()
        return xs, ys
