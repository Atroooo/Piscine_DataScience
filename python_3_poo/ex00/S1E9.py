from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True) -> None:
        """Create a new character.

        Args:
            first_name (str): first name of the character
            is_alive (bool, optional): set the character alive or not.
                Defaults to True.
        """
        assert isinstance(first_name, str), "__init__ only takes str, bool"
        assert isinstance(is_alive, bool), "__init__ only takes str, bool"
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Kill the character.
        """
        self.is_alive = False


class Stark(Character):
    """Class representing a Stark character."""

    def __init__(self, first_name, is_alive=True) -> None:
        """Create a new character.

        Args:
            first_name (str): first name of the character
            is_alive (bool, optional): set the character alive or not.
                Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """Kill the character.
        """
        self.is_alive = False
