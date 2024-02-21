for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(0, 20, 1):
    print(20 - i, end=' ')
print()

# c
number = int(input("Number of stars: "))
for i in range(number):
    print("*", end='')
print()

# d
number = int(input("Number of stars: "))
for i in range(1, number + 1):
    print("*" * i, end='')
    print()
