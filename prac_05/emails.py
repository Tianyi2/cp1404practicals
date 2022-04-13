def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)


def get_name(email):
    fullname = email.split('@')[0]
    part_of_name = fullname.split('.')
    name = " ".join(part_of_name).title()
    return name


main()
