"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    datas = get_data()
    display_subject_details(datas)


def display_subject_details(datas):
    for subject in range(len(datas)):
        print(f"{datas[subject][0]} is taught by {datas[subject][1]:<12} and has {datas[subject][2]:>3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []
    input_file = open(FILENAME)
    for line in input_file:
        parts = line.strip().split(',')  # Remove the \n
        parts[2] = int(parts[2])
        subject_details.append(parts)
    input_file.close()
    return subject_details


main()