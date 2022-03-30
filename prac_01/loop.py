# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
stars_number = int(input("Number of stars: "))
for i in range(stars_number):
    print("*", end="")
print()

# d.
stars_number = int(input("Number of stars: "))
for i in range(stars_number):
    for j in range(i + 1):
        print("*", end="")
    print()
