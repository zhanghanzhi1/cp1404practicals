import datetime


class Project:
    """Represents a project with its details."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a new project."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Compare two projects by priority (for sorting)."""
        return self.priority < other.priority

    def is_completed(self):
        """Return True if the project is completed."""
        return self.completion_percentage == 100

    def is_incomplete(self):
        """Return True if the project is incomplete."""
        return self.completion_percentage < 100

    def update(self, completion_percentage=None, priority=None):
        """Update the project's completion percentage and/or priority."""
        if completion_percentage is not None:
            self.completion_percentage = completion_percentage
        if priority is not None:
            self.priority = priority
