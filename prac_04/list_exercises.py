numbers = []
NUMBER_OF_NUMBERS = 5

while len(numbers) < NUMBER_OF_NUMBERS:
    try:
        number = int(input("Number: "))
        numbers.append(number)
    except ValueError:
        print("Invalid input, please enter an integer.")

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers)/len(numbers):,.1f}")


print("\n")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

input_username = input("Please enter the username: ")

if input_username in usernames:
    print("Access granted")
else:
    print("Access denied")
