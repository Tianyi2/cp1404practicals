class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        return 2022 - self.year

    def is_vintage(self):
        return True if self.get_age() > 50 else False

    def vintage_string(self):
        return True if self.is_vintage() else False

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"
