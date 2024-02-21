"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

MINIMUM_VALID = 0
MAXIMUM_VALID = 100

score = float(input("Enter score: "))
while score < MINIMUM_VALID or score > MAXIMUM_VALID:
    print("Invalid score")
    score = float(input("Enter score: "))

if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Bad")
