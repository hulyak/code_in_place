colors = ["Red", "Green", "Blue", "Yellow", "Orange"]

# enumerate(colors)

list(enumerate(colors))

# tuple unpacking
for index, color in enumerate(colors):
    print(index, color)


# DICTIONARIES
hex_colors = {
    "Red": "#FF0000",
    "Green": "#008000",
    "Blue": "#0000FF",
}

print(hex_colors.items())  # returns tuple

# tuple unpacking
for key, value in hex_colors.items():
    print(key, value)
