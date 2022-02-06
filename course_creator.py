from typing import Any, List, Union, Tuple

import re

import parsers.parse_timetable as pt
from course.course import Course
from course.course import Practical
from course.course import Tutorial
from course.lecture import Lecture


REMOVE_HTML = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')


def create_course(code: str, section: str) -> Course:
    """
    Creates a new course with the given code.
    """
    # Get course timetable
    timetable = pt.search_timetable(code)

    timetable_keys = ' '.join(list(timetable.keys()))
    flag = False
    if f"-{section}-" not in timetable_keys:
        flag = True

    if flag:
        raise ValueError("Section not found.")

    # Get course description
    description = pt.get_description(section, timetable)
    description = re.sub(REMOVE_HTML, '', description)

    # Get course prerequisites
    prereqs = pt.get_prereqs(section, timetable)

    # Get course corequisites
    coreqs = pt.get_coreqs(section, timetable)

    # Get course exclusions
    exclusions = pt.get_exclusions(section, timetable)

    # Get course breadth
    breadth = pt.get_breadth(section, timetable)

    # Get code of specific sessional offering
    offering = next(filter(lambda x: section.upper() in x, timetable.keys()))

    # Create set of possible meeting types (LEC/TUT/PRA)
    meeting_types = set(map(lambda x: x.upper()[:3],
                            timetable[offering]['meetings']))

    # For each meeting type, create either a new Lecture, Practical, or Tutorial
    lecs, pras, tuts = create_meetings(meeting_types, section, timetable)

    return Course(code, timetable[offering]['courseTitle'], section, description, prereqs,
                  coreqs, exclusions, breadth, lecs,
                  tuts, pras)


def create_meetings(meeting_types, section, timetable) -> Tuple[
    Union[List[Any], List[Lecture]], Union[List[Any], List[Lecture]], Union[
        List[Any], List[Lecture]]]:
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
