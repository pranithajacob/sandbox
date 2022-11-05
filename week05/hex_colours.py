"""
color names in a dictionary
"""


COLOR_TO_NAME_TO_COLOR_CODE = {
    "absolute zero": "#0048ba",
    "alice blue": "#f0f8ff",
    "baby blue": "#89cff0",
    "blue 1": "#0000ff",
    "cameo pink": "#efbbcc",
    "brilliant rose": "#ff55a3",
    "apricot": "#fbceb1",
    "amber": "#ffbf00",
    "bitter lemon": "#cae00d",
    "beaver": "#9f8170"
}
print(COLOR_TO_NAME_TO_COLOR_CODE)

color_name = input("Enter color name:(hit enter to quit): ").lower()
while color_name != "":
    if color_name in COLOR_TO_NAME_TO_COLOR_CODE:
        print(color_name, "is", COLOR_TO_NAME_TO_COLOR_CODE[color_name])
    else:
        print("Invalid color name")
    state_code = input("Enter colour name :(hit enter to quit): ").lower()
print("Bye.")

