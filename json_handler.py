import json
import os


def open_config(config):
    # open's config file in notepad for editing
    path = os.path.join(r"./Profiles/" + config)
    os.system("notepad " + path)


def keys_exists(element, *keys):
    if not isinstance(element, dict):
        raise AttributeError('keys_exists() expects dict as first argument.')

    if len(keys) == 0:
        raise AttributeError(
            'keys_exists() expects at least two arguments, one given.')

    _element = element

    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return False
    return True


def safe_get_path(element, *keys):
    for key in keys:
        try:
            element = element[key]
        except KeyError:
            return None
    return element


def get_dict(config):
    file_location = f"./Profiles/{config}"
    with open(file_location, 'r') as file:
        keys_dict = json.load(file)
    return keys_dict


class JsonHandler:
    def __init__(self):
        pass

    def save_key(self, key, config):
        dict = get_dict(config)

        pass

    def create_config(self):
        # generates a new config file
        pass
