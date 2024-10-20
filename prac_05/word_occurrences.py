"""
Word Occurrences
Estimate: 30 minutes
Actual:   37 minutes
"""


def main():
    """Get user input, calculate and print word counts."""
    user_input = input("Enter a string: ")
    word_count = count_words(user_input)
    print_word_counts(word_count)


def count_words(text):
    """Count occurrences of each word in the input text."""
    words = text.split()

    word_count = {}

    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def print_word_counts(word_count):
    """Print the word counts in a formatted and sorted manner."""
    max_length = max(len(word) for word in word_count)

    for word in sorted(word_count):
        print(f"{word:{max_length}} : {word_count[word]}")


main()
