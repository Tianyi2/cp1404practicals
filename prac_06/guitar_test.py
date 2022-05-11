from prac_06.guitar import Guitar

guitar = Guitar(name="Gibson L-5 CES", year=1922, cost=16035.40)
other = Guitar(name="Another Guitar", year=2013, cost=1512.9)

print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}")
print(f"{other.name} get_age() - Expected 10. Got {other.get_age()}")
print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
print(f"{guitar.name} is_vintage() - Expected False. Got {other.is_vintage()}")
