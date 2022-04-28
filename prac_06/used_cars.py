"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "my_car")
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    print(f"Car {{{my_car.fuel}}} {{{my_car.odometer}}}")

main()

# 1.
limo = Car(fuel=100, name="limo")
# 2.
limo.add_fuel(20)
# 3.
print(f"Fuel is {limo.fuel}")
# 4.
limo.drive(115)
# 5.
print(f"Odometer is {limo.odometer}")
# 6.
print(limo)

