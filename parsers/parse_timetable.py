import json
from typing import List, Dict

import requests

URL = "https://timetable.iit.artsci.utoronto.ca/api/20219/courses?org=&code="


def search_timetable(code: str) -> json:
    """Search for a timetable on the artsci website."""
    url = URL + code
    response = requests.get(url)
    return response.json()


def get_sessions(type: str, section: str, timetable: json) -> List[str]:
    """Get all <type> sessions from the <timetable>."""
    # Get course ID for the session given
    offering = next(filter(lambda x: section.upper() in x, timetable.keys()))
    sessions = []
    # Find if type.upper() is in the content of the keys
    meeting_types = set(map(lambda x: x.upper()[:3], timetable[offering]['meetings']))
    if type.upper() in meeting_types:
        for meeting in timetable[offering]["meetings"].keys():
            if type.upper() in meeting:
                sessions.append(meeting)
        return sessions
    else:
        return []


def get_times(session: str, section: str, timetable: json) -> Dict[str,
                                                                   List[str]]:
    """Get all times for a given session."""
    offering = next(filter(lambda x: section.upper() in x, timetable.keys()))
    schedule = timetable[offering]["meetings"][session]["schedule"]

    # Get codes for each time offered
    times = list(schedule.keys())

    times_dict = {}
    for time in times:
        meeting_day = schedule[time]["meetingDay"]
        meeting_start = schedule[time]["meetingStartTime"]
        meeting_end = schedule[time]["meetingEndTime"]
        meeting_location = schedule[time]["assignedRoom1"]
        if meeting_location is None:
            meeting_location = schedule[time]["assignedRoom2"]
        times_dict[time] = [meeting_day, meeting_start, meeting_end,
                            meeting_location]

    return times_dict


def get_instructors(session: str, section: str, timetable: json) -> \
                    List[str]:
    """Get all instructors for a given session."""
    offering = next(filter(lambda x: section.upper() in x, timetable.keys()))
    instructors = timetable[offering]["meetings"][session]["instructors"]

    # Get codes for each instructor
    instructors_list = []
    for instructor in instructors:
        instructor = instructors[instructor]["firstName"] + " " + \
                     instructors[instructor]["lastName"]
        instructors_list.append(instructor)

    return instructors_list


if __name__ == '__main__':
    # Get the timetable for the course
    timetable = search_timetable(input("Enter course code: "))

    # Get all lecture sessions
    section = input("Enter section (F/S): ")
    type = input("Enter type (LEC/TUT/PRA): ")
    sessions = get_sessions(type, section, timetable)
    if sessions:
        i = 0
        for session in sessions:
            print(f"Session {i}: {session}")
            i += 1

        session = input("Enter session number: ")

        # Get times for the chosen session
        times = get_times(sessions[int(session)], section, timetable)

        # Print the times
        print("=" * 20 + "\n" + "Times:")
        for time in times:
            print(f"{times[time][0]}: {times[time][1]} - {times[time][2]}")
        print("=" * 20)

        # Get instructors for the chosen session
        instructors = get_instructors(sessions[int(session)], section, timetable)

        # Print the instructors
        print("Instructors:")
        for instructor in instructors:
            print(f"{instructor}")
        print("=" * 20)

        # Print the location
        print("Location:")
        print(f"{times[list(times.keys())[0]][3]}")
    else:
        print("No sessions found")
