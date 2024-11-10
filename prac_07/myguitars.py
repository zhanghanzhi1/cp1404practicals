import csv
from guitar import Guitar


def read_guitars_from_file(filename):
    """Reads the guitar data from a CSV file and returns a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display all guitars in the list."""
    for guitar in guitars:
        print(guitar)


def add_new_guitar(guitars):
    """Prompt the user to enter a new guitar and add it to the list."""
    print("\nEnter a new guitar:")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)


def write_guitars_to_file(filename, guitars):
    """Write the list of guitars to the CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    """Main function to read, display, sort guitars, and handle user input."""
    guitars = read_guitars_from_file("guitars.csv")
    print("All Guitars:")
    display_guitars(guitars)

    # Sorting the guitars by year
    guitars.sort()
    print("\nSorted Guitars by Year:")
    display_guitars(guitars)

    # Adding new guitars from user input
    add_new_guitar(guitars)

    # Displaying the updated list
    print("\nUpdated List of Guitars:")
    display_guitars(guitars)

    # Writing the updated list back to the file
    write_guitars_to_file("guitars.csv", guitars)


if __name__ == "__main__":
    main()
