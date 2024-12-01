from guitar import Guitar


def main():
    """Test the Guitar class methods."""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 765.40)

    # Testing get_age()
    expected_age1 = 100
    actual_age1 = guitar1.get_age()
    print(f"{guitar1.name} get_age() - Expected {expected_age1}. Got {actual_age1}")

    expected_age2 = 9
    actual_age2 = guitar2.get_age()
    print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {actual_age2}")

    # Testing is_vintage()
    expected_vintage1 = True
    actual_vintage1 = guitar1.is_vintage()
    print(f"{guitar1.name} is_vintage() - Expected {expected_vintage1}. Got {actual_vintage1}")

    expected_vintage2 = False
    actual_vintage2 = guitar2.is_vintage()
    print(f"{guitar2.name} is_vintage() - Expected {expected_vintage2}. Got {actual_vintage2}")


if __name__ == "__main__":
    main()
