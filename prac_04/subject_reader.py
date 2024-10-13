
FILENAME = "subject_data.txt"


def main():
    """Read data from file and display formatted."""
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    # for line in input_file:
    #     print(line)  # See what a line looks like
    #     print(repr(line))  # See what a line really looks like
    #     line = line.strip()  # Remove the \n
    #     parts = line.split(',')  # Separate the data into its parts
    #     print(parts)  # See what the parts look like (notice the integer is a string)
    #     parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
    #     print(parts)  # See if that worked
    #     print("----------")
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    """Display the data from file formatted."""
    max_length_lecturer = max(len(subject_details[1]) for subject_details in data)
    max_length_students = max(len(str(subject_details[2])) for subject_details in data)
    for subject_detail in data:
        subject_code = subject_detail[0]
        lecturer = subject_detail[1]
        number_of_students = subject_detail[2]
        print(f"{subject_code} is taught by {lecturer:<{max_length_lecturer}} and has {number_of_students:>{max_length_students}} students")


main()
