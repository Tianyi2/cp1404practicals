from prac_06.guitar import Guitar

guitars = []


def main():
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.vintage_string():
            vintage_string = "(vintage)"
        print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")




main()