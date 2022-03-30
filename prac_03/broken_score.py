"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = check_result(score)
    print(result)
    score = random.randint(0, 100)
    print(f"A random score of {score} has a result of {check_result(score)}")


def check_result(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
