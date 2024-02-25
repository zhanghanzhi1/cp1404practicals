"""MINIMUM_LENGTH = 5


function main()
    password = get_password()
    print_asterisks(password)


function get_password()
    get user_password
    while len(user_password) < MINIMUM_LENGTH
        print Try again
        get user_password

    return user_password


function print_asterisks(password)
    print '*'
    return 0

main()
"""

MINIMUM_LENGTH = 5


def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    user_password = input("Enter a password: ")
    while len(user_password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters long. Try again.")
        user_password = input("Enter a password: ")

    return user_password


def print_asterisks(password):
    print('*' * len(password))
    return 0


main()
