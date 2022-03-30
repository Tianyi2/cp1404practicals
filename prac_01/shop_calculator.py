total_price = 0
items_number = int(input("Number of items: "))
while items_number < 0:
    print("Invalid number of items!")
    items_number = int(input("Number of items: "))

for i in range(items_number):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > 100:
    total_price *= 0.9

print("Total price for {} items is ${:.2f}".format(items_number, total_price))
