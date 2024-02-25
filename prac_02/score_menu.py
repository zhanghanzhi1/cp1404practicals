"""menu = (G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit
MAXIMUM_NUMBER = 100
MINIMUM_NUMBER = 0


function main()
    get score
    display menu
    get choice
    while choice != "Q"
        if choice == "G"
            score = get_valid_score()
        else if choice == "P"
            display identify_result(score)
        else if choice == "S"
            display "*" * score
        else
            display Invalid choice
        display menu
        get choice
    display Farewell


function get_valid_score()
    get score
    while score < MINIMUM_NUMBER or score > MAXIMUM_NUMBER
        display Invalid score
        get score
    return score


function identify_result(score)
    if score >= 90
        return "Excellent"
    else if score >= 50
        return "Pass"
    else
        return "Bad"


main()
"""





menu = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""
MAXIMUM_NUMBER = 100
MINIMUM_NUMBER = 0


def main():
    score = get_valid_score()
    print(menu)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(identify_result(score))
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice.")
        print(menu)
        choice = input(">>>").upper()
    print("Farewell.")


def get_valid_score():
    score = int(input("Please enter the score:"))
    while score < MINIMUM_NUMBER or score > MAXIMUM_NUMBER:
        print("Invalid score.")
        score = int(input("Please enter the score:"))
    return score


def identify_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
