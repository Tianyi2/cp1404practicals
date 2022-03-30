# 1.
name = input("What is your name?: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2.
in_file = open("name.txt", "r")
print(f"Your name is {in_file.read().strip()}")
in_file.close()

# 3.
in_file = open("numbers.txt", "r")
first = int(in_file.readline())
second = int(in_file.readline())
in_file.close()
print(first + second)

# 4.
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    total += int(line)
print(total)
in_file.close()
