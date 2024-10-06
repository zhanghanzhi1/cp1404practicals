# Task 1: Writing the user's name in file
name = input("Enter your name:")
with open("name.txt", "w") as file:
    file.write(name)

# Task 2: Writing and reading the user's name
with open("name.txt", "r") as file:
    name = file.read().strip()
print(f"Your name is {name}")

# Task 3: Calculating the total number.
total = 0
with open("numbers.txt", "r") as file:
    numbers = file.readlines()[:2]
    for line in numbers:
        number = line.strip()
        total += int(number)
print(f"Total of first two number is: {total}")

# Task 4: Calculate all numbers
total = 0
with open("numbers.txt", "r") as file:
    numbers = file.readlines()
    for line in numbers:
        number = line.strip()
        total += int(number)
print(f"Total of all numbers is: {total}")
