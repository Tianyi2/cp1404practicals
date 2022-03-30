def main():
    """Get and print out password in asterisk"""
    MINIMUM_LENGTH = 9
    password = get_password(MINIMUM_LENGTH)
    print_asterisk(password)


def get_password(MINIMUM_LENGTH):
    """Get valid password"""
    password = input("What is ur password?: ")
    while len(password) < MINIMUM_LENGTH:
        password = input("What is ur password?: ")
    return password


def print_asterisk(password):
    """Print asterisk with a number of the length of password"""
    for i in range(len(password)):
        print("*", end="")


main()
