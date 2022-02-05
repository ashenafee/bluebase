from typing import Any, List, Union

import parsers.parse_timetable as pt
from course.course import Course
from course.course import Practical
from course.course import Tutorial
from course.lecture import Lecture


def create_course(code: str, section: str) -> Course:
    """
    Creates a new course with the given code.
    """
    # Get course timetable
    timetable = pt.search_timetable(code)

    # Get code of specific sessional offering
    offering = next(filter(lambda x: section.upper() in x, timetable.keys()))

    # Create set of possible meeting types (LEC/TUT/PRA)
    meeting_types = set(map(lambda x: x.upper()[:3],
                            timetable[offering]['meetings']))

    # For each meeting type, create either a new Lecture, Practical, or Tutorial
    lecs, pras, tuts = create_meetings(meeting_types, section, timetable)

    return Course(code, timetable[offering]['courseTitle'], section, lecs,
                  tuts, pras)


def create_meetings(meeting_types, section, timetable) -> tuple[
    Union[list[Any], list[Lecture]], Union[list[Any], list[Lecture]], Union[
        list[Any], list[Lecture]]]:
    """Create and return list of meetings of the given type."""
    lecs = []
    tuts = []
    pras = []
    for meeting_type in meeting_types:
        if meeting_type == 'LEC':
            lecs = list_of_meetings(meeting_type, section, timetable)
        elif meeting_type == 'TUT':
            tuts = list_of_meetings(meeting_type, section, timetable)
        elif meeting_type == 'PRA':
            pras = list_of_meetings(meeting_type, section, timetable)
    return lecs, pras, tuts


def list_of_meetings(meeting_type, section, timetable) -> List[Lecture]:
    """Create and return list of meetings of the given type."""
    meeting_list = pt.get_sessions(meeting_type, section, timetable)
    meetings = []
    offering = next(filter(lambda x: section.upper() in x, timetable.keys()))
    for meet in meeting_list:
        schedule = timetable[offering]["meetings"][meet]["schedule"]
        if not schedule:
            continue
        times = pt.get_times(meet, section, timetable)
        inst = pt.get_instructors(meet, section, timetable)
        loc = times[list(times.keys())[0]][3]

        if meeting_type == 'LEC':
            meetings.append(Lecture(meet, times, inst, loc))
        elif meeting_type == 'TUT':
            meetings.append(Tutorial(meet, times, inst, loc))
        elif meeting_type == 'PRA':
            meetings.append(Practical(meet, times, inst, loc))

    return meetings


if __name__ == '__main__':
    course = create_course(input("Course code:\t"), input("Section:\t\t"))
    print()
    print(course)
