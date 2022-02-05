from typing import List

from lecture import Lecture
from tutorial import Tutorial
from practical import Practical


class Course:
    """A class to represent a course being offered. Information contained in
    this class includes:
        - Course code
        - Course name
        - Course section
        - Course LEC sections
        - Course TUT sections
        - Course PRA sections
    Each LEC/TUT/PRA entry also has associated information:
        - Meeting days
        - Meeting times
        - Meeting location
        - Meeting instructor
    """

    def __init__(self, code: str, name: str, section: str, lec: List[Lecture],
                 tut: List[Tutorial], pra: List[Practical]):
        """Initialize a Course object."""
        self.code = code
        self.name = name
        self.section = section
        self.lec = lec
        self.tut = tut
        self.pra = pra


