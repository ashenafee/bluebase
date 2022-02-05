import json
import requests

URL = "https://timetable.iit.artsci.utoronto.ca/api/20219/courses?org=&code="


def search_timetable(code: str) -> json:
    """Search for a timetable on the artsci website."""
    url = URL + code
    response = requests.get(url)
    return response.json()


def get_sessions(type: str, timetable: json) -> list:
    """Get all <type> sessions from the <timetable>."""
    sessions = []
    for meeting in timetable[timetable]["meetings"].keys():
        if type in meeting:
            sessions.append(meeting)
    return sessions


if __name__ == '__main__':
    #print(search_timetable('CSC207')['CSC207H1-F-20219']['courseId'])
    print(get_sessions('LEC', search_timetable('CHM136')))
