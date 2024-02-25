"""
CP1404/CP5632 - Practical


MINIMUM_VALID = 0
MAXIMUM_VALID = 100


function main()
    get score
    while score < MINIMUM_VALID or score > MAXIMUM_VALID
        display Invalid
        get score
    result = identify_result(score)
    display result
    random_number = random.randint(0, 100)
    random_result = identify_result(random_number)
    display random_number, random_result


function identify_result(score)
    if score >= 90
        return "Excellent"
    else if score >= 50
        return "Pass"
    else
        return "Bad"


main()

"""
import random

MINIMUM_VALID = 0
MAXIMUM_VALID = 100


def main():
    score = float(input("Enter score: "))
    while score < MINIMUM_VALID or score > MAXIMUM_VALID:
        print("Invalid score")
        score = float(input("Enter score: "))
    result = identify_result(score)
    print(result)
    random_number = random.randint(0, 100)
    random_result = identify_result(random_number)
    print(random_number, "\n", random_result, sep="")


def identify_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
