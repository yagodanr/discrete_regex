from __future__ import annotations
from abc import ABC, abstractmethod

from queue import LifoQueue


class State(ABC):


    @abstractmethod
    def __init__(self) -> None:
        self.next_states: list[State] = []

    @abstractmethod
    def check_self(self, char: str) -> bool:
        """
        function checks whether occured character is handled by current ctate
        """
        pass

    def get_self(self) -> set[State]:
        return {self}

    def check_next(self, next_char: str) -> State | Exception:
        next_states = set()
        for state in self.next_states:
            for n in state.get_self():
                if n.check_self(next_char):
                    next_states.add(n)
            # if state.check_self(next_char):
            #     next_states |= state.get_self()
        return next_states

class StartState(State):

    def __init__(self):
        super().__init__()

    def check_self(self, char: str):
        return True


class TerminationState(State):
    """
    state for end of string
    """

    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TerminationState, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
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

    def __init__(self, symbol: str) -> None:
        super().__init__()
        self.curr_sym = symbol

    def check_self(self, curr_char: str) -> State | Exception:
        return self.curr_sym == curr_char


class StarState(State):

    def __init__(self, checking_state: State):
        super().__init__()
        self.next_states.append(checking_state)

    def check_self(self, char: str):
        return True

    def get_self(self) -> set[State]:
        """
        function returns all states that are accepted by current state
        """
        s = set()
        for state in self.next_states:
            s |= state.get_self()
        return s|{self}

    def check_next(self, next_char):
        return super().check_next(next_char)


class PlusState(State):

    def __init__(self, checking_state: State):
        super().__init__()
        self.next_states.append(checking_state)

    def check_self(self, char: str):
        return True

    def get_self(self) -> set[State]:
        """
        function returns all states that are accepted by current state
        """
        s = set()
        for state in self.next_states:
            s |= state.get_self()
        return s|{self}

    def check_next(self, next_char):
        return super().check_next(next_char)


class CharactersState(State):
    def __init__(self, symbols: str) -> None:
        super().__init__()
        self.symbols = set()
        self.add_symbols(symbols)


    def add_symbols(self, symbols: str) -> None:
        i = 0
        while i < len(symbols):
            if symbols[i] == "-":
                for j in range(ord(symbols[i-1]), ord(symbols[i+1])+1):
                    self.symbols.add(chr(j))
            else:
                self.symbols.add(symbols[i])
            i += 1

    def check_self(self, curr_char: str) -> State | Exception:
        return curr_char in self.symbols



class RegexFSM:
    """
    https://medium.com/@phanindramoganti/regex-under-the-hood-implementing-a-simple-regex-compiler-in-go-ef2af5c6079
    """


    def __init__(self, regex_expr: str) -> None:
        self.curr_state: State = StartState()
        prev_state = self.curr_state

        stack = LifoQueue()
        stack.put(self.curr_state)
        bracket_state = False
        brackets_string = ""
        for char in regex_expr:
            new_state = None

            if bracket_state:
                if char == "]":
                    new_state = CharactersState(brackets_string)
                    bracket_state = False
                    brackets_string = ""
                else:
                    brackets_string += char
                    continue


            if char == "[":
                bracket_state = True
                continue

            elif char == ".":
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

            elif char.isalnum():
                new_state = AsciiState(char)

            if new_state is None:
                raise AttributeError("Character is not supported")

            prev_state.next_states.append(new_state)
            prev_state = new_state
            stack.put(new_state)

        last_state = stack.get()
        last_state.next_states.append(TerminationState())


    def check_string(self, string: str) -> bool:
        """
        function checks whether string is accepted by regex
        """
        prev_states = {self.curr_state}
        for char in string:
            new_states = set()
            for state in prev_states:
                try:
                    new_states |= state.check_next(char)
                except NotImplementedError:
                    pass
            if len(new_states) == 0:
                return False
            prev_states = new_states
        new_states = set()
        for state in prev_states:
            try:
                new_states |= state.check_next(char)
            except NotImplementedError:
                pass
        if len(new_states) == 0:
            return False
        if TerminationState() in new_states:
            return True
        return TerminationState() in prev_states


if __name__ == "__main__":
    regex_pattern = "a*4.+hi"

    regex_compiled = RegexFSM(regex_pattern)

    print(regex_compiled.check_string("aaaaaa4uhi"))  # True
    print(regex_compiled.check_string("4uhi"))  # True
    print(regex_compiled.check_string("a4uhi"))  # True
    print(regex_compiled.check_string("a4uhhi"))  # True
    print(regex_compiled.check_string("meow"))  # False