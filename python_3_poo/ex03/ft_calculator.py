class calculator:
    """A simple calculator class that can add, multiply, subtract and divide.
    """
    def __init__(self, vector) -> None:
        """__init__ method for calculator class.

        Args:
            vector (vector): A list of numbers.
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """__add__ method for calculator class that add a number
            to the vector.

        Args:
            object (int): A number to add to the vector.
        """
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """__mul__ method for calculator class that multiplies the vector
            by a number.

        Args:
            object (int): A number to multiply the vector by.
        """
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """__sub__ method for calculator class that substracts a number
            to the vector.

        Args:
            object (int): A number to subtract from the vector.
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """__truediv__ method for calculator class that divides the vector

        Args:
            object (int): A number to divide the vector by.

        Raises:
            ZeroDivisionError: If the object is 0, raise an error.
        """
        try:
            if object == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)
