"""
MENU = C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius

valid_choice = ["C", "F"]
print MENU
get choice
while choice not in valid_choice
    print Invalid option
    print MENU
    get choice


function main()
    if choice == "C"
        get celsius
        fahrenheit = convert_c_to_f(celsius)
        print fahrenheit

    else
        get fahrenheit
        celsius = convert_f_to_c(fahrenheit)
        print celsius


function c_to_f(celsius)
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


function f_to_c(fahrenheit)
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
"""
valid_choice = ["C", "F"]
print(MENU)
choice = input(">>> ").upper()
while choice not in valid_choice:
    print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()


def main():
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = convert_c_to_f(celsius)
        print(f"Fahrenheit: {fahrenheit:.2f} F")

    else:
        fahrenheit = float(input("Fahrenheit: "))
        celsius = convert_f_to_c(fahrenheit)
        print(f"Celsius: {celsius:.2f} C")


def convert_c_to_f(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_f_to_c(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
