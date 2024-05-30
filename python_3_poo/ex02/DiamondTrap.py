from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The false King"""
    def __init__(self, first_name, is_alive=True):
        """Create a new King.

        Args:
            first_name (str): first name of the character
            is_alive (bool, optional): set the character alive or not.
                Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """Set the color of the eyes.

        Args:
            color (str): color of the eyes.
        """
        self.eyes = color

    def set_hairs(self, color):
        """Set the color of the hairs.

        Args:
            color (str): color of the hairs.
        """
        self.hairs = color

    def get_eyes(self):
        """Get the color of the eyes.

        Returns:
            str: eyes color
        """
        return self.eyes

    def get_hairs(self):
        """Get the color of the hairs.

        Returns:
            str: hairs color
        """
        return self.hairs
