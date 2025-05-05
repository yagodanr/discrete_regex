from __future__ import annotations
from abc import ABC, abstractmethod

from queue import LifoQueue


class State(ABC):
    next_states: list[State] = []

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def check_self(self, char: str) -> bool:
        """
        function checks whether occured character is handled by current ctate
        """
        pass

    def check_next(self, next_char: str) -> State | Exception:
        for state in self.next_states:
            if state.check_self(next_char):
                return state
        raise NotImplementedError("rejected string")


class StartState(State):
    next_states: list[State] = []

    def __init__(self):
        super().__init__()

    def check_self(self, char:str):
        return super().check_self(char)


class TerminationState(State):
    """
    state for end of string
    """

    next_states: list[State] = []

    def __init__(self):
        self.next_states.append(self)

    def check_self(self, char: str):
        return True


class DotState(State):
    """
    state for . character (any character accepted)
    """

    next_states: list[State] = []

    def __init__(self):
        super().__init__()

    def check_self(self, char: str):
        return True  # any character is accepted


class AsciiState(State):
    """
    state for alphabet letters or numbers
    """

    next_states: list[State] = []

    def __init__(self, symbol: str) -> None:
        self.curr_sym = symbol

    def check_self(self, curr_char: str) -> State | Exception:
        return self.curr_sym == curr_char


class StarState(State):

    next_states: list[State] = []

    def __init__(self, checking_state: State):
        self.next_states.append(checking_state)

    def check_self(self, char):
        for state in self.next_states:
            if state.check_self(char):
                return True

        return False


class PlusState(State):
    next_states: list[State] = []

    def __init__(self, checking_state: State):
        self.next_states.append(checking_state)

    def check_self(self, char: str):
        for state in self.next_states:
            if state.check_self(char):
                return True

        return False


class RegexFSM:
    """
    https://medium.com/@phanindramoganti/regex-under-the-hood-implementing-a-simple-regex-compiler-in-go-ef2af5c6079
    """
    curr_state: State = StartState()

    def __init__(self, regex_expr: str) -> None:

        prev_state = self.curr_state

        stack = LifoQueue()
        stack.put(self.curr_state)
        for char in regex_expr:
            new_state = None


            if char == ".":
                new_state = DotState()
            elif char == "*":
                # make * state before the prev state
                new_state = StarState(prev_state)
                stack.get()
                prev_prev = stack.get()
                stack.put(prev_prev)
                prev_prev.next_states.pop()
                prev_prev.next_states.append(new_state)
            elif char == "+":
                new_state = PlusState(prev_state)

            elif char.isascii():
                new_state = AsciiState(char)
            else:
                raise AttributeError("Character is not supported")

            prev_state.next_states.append(new_state)
            prev_state = new_state
            stack.put(new_state)

        last_state = stack.get()
        last_state.next_states.append(TerminationState())


    def check_string(self):
        pass  # Implement


if __name__ == "__main__":
    regex_pattern = "a*4.+hi"

    regex_compiled = RegexFSM(regex_pattern)

    print(regex_compiled.check_string("aaaaaa4uhi"))  # True
    print(regex_compiled.check_string("4uhi"))  # True
    print(regex_compiled.check_string("meow"))  # False