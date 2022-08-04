import json


path_to_json = "candidates.json"


def load_candidates(path):
    """Read data from json file.

       Args:
           path (str) = path to file

        Returns:
            List[dict]

    """
    with open(path, encoding="utf-8") as f:
        candidates = json.load(f)
    return candidates


def get_all():
    """Returns the view of all candidates

        Returns:
            Str

    """
    candidates = load_candidates(path_to_json)

    result = ""
    for candidate in candidates:
        result = result + get_format(candidate) + "\n"

    result = result.rstrip() + "\n"

    return result


def get_by_pk(pk):
    """Finds a candidate by his user ID

        Args:
            pk (int) = user id

        Returns:
            Dict{photo, info}

    """
    candidates = load_candidates(path_to_json)

    result = {}
    for candidate in candidates:
        if pk == candidate["pk"]:
            url = candidate["picture"]

            result["photo"] = f"<img src={url} alt='Candidate photo'/>"
            result["info"] = get_format(candidate)

            return result


def get_by_skill(skill_name):
    """Finds candidates by skill

        Args:
            skill_name (str) = skill

        Returns:
            str

    """
    candidates = load_candidates(path_to_json)

    skill = skill_name.lower()
    result = ""
    for candidate in candidates:
        skill_list = candidate["skills"].split(', ')
        if skill in skill_list:
            result = result + get_format(candidate) + "\n"

    result = result.rstrip() + "\n"

    return result


def get_format(candidate):
    """Returns a formatted string

            Args:
                candidate (dict) = a candidate

            Returns:
                str

    """
    result = candidate["name"] + "\n" + candidate["position"] + "\n" + candidate["skills"] + "\n"
    return result
