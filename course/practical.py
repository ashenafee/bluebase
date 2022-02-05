from typing import List

from course.meeting import Meeting


class Practical(Meeting):
    """A class to represent a practical offered by a course. Information
    includes:
        - Practical days
        - Practical times
        - Practical location
        - Practical instructor
    """

    def __init__(self, code: str, times: dict[str, List[str]],
                 instructors: List[str], location: str):
        super().__init__(code, times, instructors, location)

    def __str__(self):
        """Returns a string representation of the practical."""
        return f"{self.code}: {self.times} {self.instructors} {self.location}"
