from typing import List, Dict


class Meeting:
    """A class to represent a meeting offered by a course. Information
    includes:
        - Meeting days
        - Meeting times
        - Meeting location
        - Meeting instructor
    """

    def __init__(self, code: str, times: Dict[str, List[str]],
                 instructors: List[str], location: str):
        self.code = code
        self.times = []
        self.instructors = instructors
        if location is not None:
            self.location = location
        else:
            self.location = "NO LOCATION"
        self._format_times(times)

    def _format_times(self, times_dict) -> None:
        """Formats the times of the lecture."""
        times = []
        for day in times_dict:
            time_str = f"{times_dict[day][0]}: {times_dict[day][1]}-" \
                       f"{times_dict[day][2]}"
            times.append(time_str)
        self.times = times

    def __str__(self):
        """Returns a string representation of the meeting."""
        return f"{self.code}: {self.times} {self.instructors} {self.location}"
