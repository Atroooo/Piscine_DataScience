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

    def __str__(self):
        """__str__ method

        Returns:
            str: string representation of the object
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """__repr__ method

        Returns:
            str: representation of the object
        """
        return self.__str__()


class Stark(Character):
    """Class representing a Stark character."""

    def __init__(self, first_name, is_alive=True) -> None:
        """Create a new character from the Stark family.

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
