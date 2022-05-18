import os


def profile_selector():
    options = os.listdir(r'./Profiles')
    total_file = []
    for i in options:
        f = os.path.splitext(i)
        total_file.append(f[0])

    for file in range(len(total_file)):
        print(file, total_file[file])

    selected_file_number = int(input("\nEnter Profile number: "))

    for file in range(len(total_file)):
        if selected_file_number == file:
            selected_file = total_file[file]

    return selected_file
