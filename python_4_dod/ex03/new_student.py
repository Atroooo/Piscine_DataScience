import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generates a random 15 char long student id
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represents information about students, including their name,
        surname, active status, login, and a unique ID.

    Args:
        name (str): The first name of the student.
        surname (str): The last name or surname of the student.
        active (bool, optional): A boolean value indicating whether the
        student is active (default is `True`).
        login (str): The student's login, which is generated automatically
        based on their name and surname.
        id (str): A unique identifier for the student, generated using the
        `generate_id()` function.
    """
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """Method that generate the login and check if the 
            args passed are accepted"""
        assert isinstance(self.name, str), "name must be a string"
        assert isinstance(self.surname, str), "surname must be a string"
        self.login = self.name[0].capitalize() + self.surname.lower()
