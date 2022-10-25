
MINIMUM_LENGTH = 4


def main():
    """Get and print password."""
    password = get_password(MINIMUM_LENGTH)
    print_word(password)


def get_password(minimum_length):
    """Get password, it should meets the minimum_length requirement."""
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password


def print_word(sequence):
    """Print as many asterisks as there are characters in the passed-in sequence."""
    print('*' * len(sequence))


main()

