FILENAME: str = "subject_data.txt"


def main():

    data = get_data()
    print(data)


def get_data():

    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer
        print(parts)  # See if that worked
        data.append(parts)
    input_file.close()
    return get_data


def display_subjects(data):
    """Display data nicely."""
    for subject_data in data:
        print("{} is taught by {:12} and has {:3} students".format(*subject_data))


main()
display_subjects()
