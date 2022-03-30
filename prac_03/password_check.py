MIN_LEN = 9
password = input("What is ur password?: ")

while len(password) < MIN_LEN:
    password = input("What is ur password?: ")

for i in range(len(password)):
    print("*", end="")

