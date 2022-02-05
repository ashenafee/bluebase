from typing import List

from course.meeting import Meeting


class Tutorial(Meeting):
    """A class to represent a tutorial offered by a course. Information
    includes:
        - Meeting days
        - Meeting times
        - Meeting location
        - Meeting instructor
    """

    def __init__(self, code: str, times: dict[str, List[str]],
                 instructors: List[str], location: str):
        super().__init__(code, times, instructors, location)

    def __str__(self):
        """Returns a string representation of the tutorial."""
        return f"{self.code}: {self.times} {self.instructors} {self.location}"
