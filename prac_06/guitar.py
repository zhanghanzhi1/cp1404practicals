class Guitar:
    """Class representing a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        name: str, the name of the guitar
        year: int, the year the guitar was made
        cost: float, the cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar in years."""
        return 2022 - self.year  # Adjust the current year as needed

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50
