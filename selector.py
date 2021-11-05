import os

options = os.listdir(r'./Profiles')
total_file = []
for i in options:
    f = os.path.splitext(i)
    total_file.append(f[0])


def profile_selector():
    for i in range(len(total_file)):
        # if possible try formatting the string to beautify it
        print(i, total_file[i])

    selected_file_number = int(input("Enter Profile number:"))

    for i in range(len(total_file)):
        if selected_file_number == i:
            selected_file = total_file[i]
            # print(total_file[i])

        # else:
        #     selected_file = "meme_board"

    return selected_file


