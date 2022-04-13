COLOUR_TO_HEXADECIMAL_COLOUR = {"AliceBlue": "#f0f8ff", "Amaranth": "Amaranth", "Amber": "#ffbf00",
                                "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "Apricot": "#fbceb1",
                                "Aqua": "#00ffff", "Asparagus": "#87a96b", "Aureolin": "#fdee00", "Azure1": "#f0ffff"}

colour_name = input("Which colour are you looking for?: ")
while colour_name != "":
    try:
        print(f"The colour is {COLOUR_TO_HEXADECIMAL_COLOUR[colour_name]}")
    except KeyError:
        print("Sorry, we do not have that color")
    colour_name = input("Which colour are you looking for?: ")
