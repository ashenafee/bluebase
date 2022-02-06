import json
from typing import List


def save_to_json(channel_id: str, course_code: str) -> None:
    """
    Saves data to a JSON file.
    """
    with open('database.json', 'r+') as f:
        f_data = json.load(f)
        try:
            f_data[str(channel_id)].append(course_code)
            f_data[str(channel_id)] = list(set(f_data[str(channel_id)]))
        except KeyError:
            f_data[channel_id] = [course_code]
            f_data[channel_id] = list(set(f_data[channel_id]))
        f.seek(0)
        json.dump(f_data, f, ensure_ascii=False, indent=4)


def remove_from_json(channel_id: str, course_code: str) -> None:
    """
    Removes data from a JSON file.
    """
    f_data = json.load(open('database.json'))
    try:
        f_data[str(channel_id)].remove(course_code)
        print("Removed course code: " + course_code)
    except ValueError:
        pass

    open('database.json', 'w').write(json.dumps(f_data, indent=4,
                                                sort_keys=True,
                                                ensure_ascii=False,
                                                separators=(',', ': ')))


def get_from_json(channel_id: str) -> List[str]:
    """
    Gets data from a JSON file.
    """
    with open('database.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data[str(channel_id)]


if __name__ == '__main__':
    save_to_json('939616612758224909', 'CSC207')
    save_to_json('939616612758224909', 'CSC209')
    save_to_json('939616612758224909', 'CSC148')
    save_to_json('939616612758224909', 'CHM136')
    remove_from_json('939616612758224909', 'CSC207')
    print(get_from_json('939616612758224909')[0])