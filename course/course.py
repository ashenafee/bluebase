from typing import List

from course.lecture import Lecture
from course.tutorial import Tutorial
from course.practical import Practical


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
        self.code = code.upper()
        self.name = name
        self.section = section.upper()
        self.lec = lec
        self.tut = tut
        self.pra = pra

    def __str__(self):
        """Return a string representation of the Course object."""
        # String representation of self.lec
        course_str = f"{self.code}{self.section} - {self.name}\n"

        if self.lec:
            for lec in self.lec:
                course_str += "LEC:\t" + str(lec) + "\n"
        if self.tut:
            for tut in self.tut:
                course_str += "TUT:\t" + str(tut) + "\n"
        if self.pra:
            for pra in self.pra:
                course_str += "PRA:\t" + str(pra) + "\n"

        return course_str


if __name__ == "__main__":
    pass
