import json
import simpleaudio as sa
import pynput
from pynput.keyboard import Listener, Key
from selector import profile_selector


print("Audio Board v0.1\n")
print("Select Profile From the following list ")

# selecting a file from selector.py and load it here

file_name = profile_selector()
print("press 'Esc' key to exit ")
print('"'+file_name+'"', "Selected")
print("Start Typing . . .")


with open("./Profiles/{}.json".format(file_name)) as f:
    data = json.load(f)


def on_press(key):
    k = str(key)
    if k.find('enter') > 0:
        sa.WaveObject.from_wave_file(r"{}".format(data["enter"])).play()

    elif key == Key.backspace:
        sa.WaveObject.from_wave_file(
            r"{}".format(data["backspace"])).play()

    elif k.find('space') > 0:
        sa.WaveObject.from_wave_file(
            r"{}".format(data["space"])).play()

    elif k.find('caps_lock') > 0:
        sa.WaveObject.from_wave_file(r"{}".format(data["capslock"])).play()

    else:
        sa.WaveObject.from_wave_file(r"{}".format(data["other_keys"])).play()


def on_release(key):
    if key == Key.esc:
        print("\nExiting . . . \nAudio Board v0.1")
        print("\nContact Developer: \nsayyedsalman2000@gmail.com")
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
