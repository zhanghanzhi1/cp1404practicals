COLOR_CODES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

print("Enter a color name to get its hexadecimal code. Leave blank to exit.")

color_name = input("Enter color name: ").strip()
while color_name != "":
    color_name_upper = color_name.capitalize()

    try:
        print(f"{color_name} has the code: {COLOR_CODES[color_name_upper]}")

    except KeyError:
        print("Invalid color name. Please try again.")

    color_name = input("Enter color name: ").strip()
