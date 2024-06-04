from S1E9 import Character


class Baratheon(Character):
    """Class representing the Baratheon family.
    """

    def __init__(self, first_name, is_alive=True):
        """Create a new character from the Baratheon family.

        Args:
            first_name (str): first name of the character
            is_alive (bool, optional): set the character alive or not.
                Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Kill the character.
        """
        self.is_alive = False


class Lannister(Character):
    """Class representing a Lannister character.
    """
    def __init__(self, first_name, is_alive=True):
        """Create a new character from the Lannister family.

        Args:
            first_name (str): _description_
            is_alive (bool, optional): _description_. Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Kill the character.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a new character from the Lannister family and return it

        Args:
            first_name (str): first name of the character
            is_alive (bool, optional): set the character alive or not.
                Defaults to True.

        Returns:
            Lannister object: return a new Lannister character.
        """
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance
