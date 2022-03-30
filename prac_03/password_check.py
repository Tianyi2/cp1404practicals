def main():
    MIN_LENGTH = 9
    password = get_password(MIN_LENGTH)
    print_asterisk(password)


def get_password(MIN_LENGTH):
    password = input("What is ur password?: ")
    while len(password) < MIN_LENGTH:
        password = input("What is ur password?: ")
    return password


def print_asterisk(password):
    for i in range(len(password)):
        print("*", end="")

main()
