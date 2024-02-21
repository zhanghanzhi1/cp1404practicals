

MINIMUM = 0
price = 0
total_price = 0
number = int(input("Number of items: "))
while number < MINIMUM:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(1, number + 1):
    price = float(input("Price of item: "))
    total_price = total_price + price
if total_price > 100:
    total_price = 0.9 * total_price
print("Total price for ", number, " items is $", round(total_price, 2), sep="")
