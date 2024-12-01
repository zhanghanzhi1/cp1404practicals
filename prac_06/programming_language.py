class ProgrammingLanguage:
    """Class representing a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance.

        name: str, name of the programming language
        typing: str, typing style (Static or Dynamic)
        reflection: bool, whether the language supports reflection
        year: int, the year the language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed, False otherwise."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
