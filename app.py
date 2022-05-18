import simpleaudio as sa
from pynput.keyboard import Key, Listener
import selector
import json_handler as jh


print("Fun-Keyboard v1.0")
print("select an audio profile")
profile = selector.profile_selector()
keys_dict = jh.get_dict(profile+".json")

print("< Press Esc to close >")
print("Running . . .")

# assistive methods


def check_type(d, key):

    _key = str(key)
    num_key = d["num-keys"]
    alpha_key = d["alphabet-keys"]
    special = d["special-keys"]

    for items in num_key:
        if _key == items:
            return "NUM_KEY"

    for items in alpha_key:
        if _key == items:
            return "ALPHA_KEY"

    return "special"


def safe_get(element, *keys):
    for key in keys:
        try:
            element = element[key]
        except KeyError:
            return None
    return element


def play_audio(path):
    sa.WaveObject.from_wave_file(path).play()


def keys_exists(element, *keys):
    """
    Check if *keys (nested) exists in `element` (dict).
    """
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


# Execution Begins here

def on_press(key):

    if keys_exists(keys_dict, "special-keys", str(key)):
        value = safe_get(keys_dict, "special-keys", str(key))
        if value != "" and value is not None:
            play_audio(value)
        else:
            value = safe_get(keys_dict, "special-keys", "default")
            play_audio(value)

    elif keys_exists(keys_dict, "num-keys", str(key)):
        value = safe_get(keys_dict, "num-keys", str(key))
        if value != "" and value is not None:
            play_audio(value)
        else:
            value = safe_get(keys_dict, "num-keys", "default")
            play_audio(value)

    elif keys_exists(keys_dict, "alphabet-keys", str(key)):
        value = safe_get(keys_dict, "alphabet-keys", str(key))
        if value != "" and value is not None:
            play_audio(value)
        else:
            value = safe_get(keys_dict, "alphabet-keys", "default")
            play_audio(value)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
