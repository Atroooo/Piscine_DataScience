class calculator:
    """Static class that allows to calculate the dot product,
        add and subtract 2 vectors
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Static method that calculates the dot product
        """
        print("Dot product is :", sum([an*bn for an, bn in zip(V1, V2)]))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Static method that adds 2 vector
        """
        result = [float(x + y) for x, y in zip(V1, V2)]
        print("Add vector is :", result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Static method that subtracts 2 vectors
        """
        result = [float(x - y) for x, y in zip(V1, V2)]
        print("Sous vector is :", result)
