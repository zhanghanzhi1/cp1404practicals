from programming_language import ProgrammingLanguage


def main():
    """Demo test code to show how to use the ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print the string representation of Python
    print(python)

    # Create a list of ProgrammingLanguage objects
    languages = [python, ruby, visual_basic]

    # Print dynamically typed languages
    print("The dynamically typed languages are:")
    for lang in languages:
        if lang.is_dynamic():
            print(lang.name)


if __name__ == "__main__":
    main()
