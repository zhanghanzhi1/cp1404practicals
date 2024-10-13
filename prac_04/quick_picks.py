import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_PICK = 6
MINIMUM_NUMBER_OF_LINES = 1


def main():
    """Get the number of lines, generates the quick pick numbers, and displays the result."""
    number_of_lines = get_valid_lines()
    quick_pick = get_full_data(number_of_lines)
    display_result(quick_pick)


def get_valid_lines():
    """Get a valid number of lines from the user."""
    valid_data = False
    while not valid_data:
        try:
            number_of_lines = int(input("How many quick picks? "))
            if number_of_lines < MINIMUM_NUMBER_OF_LINES:
                print("Invalid input.")
            else:
                valid_data = True
        except ValueError:
            print("Invalid input.")
    return number_of_lines


def get_full_data(number_of_lines):
    """Generate the specified number of quick pick lottery numbers."""
    quick_pick = []
    for m in range(number_of_lines):
        lines = []
        while len(lines) < NUMBERS_PER_PICK:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            if number not in lines:
                lines.append(number)
        quick_pick.append(sorted(lines))
    return quick_pick


def display_result(quick_pick):
    """Display the generated quick pick lottery numbers."""
    for line in quick_pick:
        print(" ".join(f"{number:2}" for number in line))


main()
