def main():
    """Create dictionary of emails-to-names."""
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        name = get_name_from_email(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    """Extract expected name from email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()


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


"""
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")


state = input("Enter short state: ").upper()
while state != "":
    if state in state_code:
        print(state, "is", state_code[state])
    if state in CODE_TO_NAME:
        print(state, "is", CODE_TO_NAME[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()



FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file and print details about Wimbledon champions and countries."""
    records = open(FILENAME)
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def process_records(records):
    """Create dictionary of champions and set of countries from records (list of lists)."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_records(filename):
    """Get records from file in list of lists form."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove header
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()

my_list = ["Text: this is a collection of words of nice words this is a fun thing it is"]
print(my_list)

unique_words = {}
word_to_count = {}
text = input(" ")

# text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()

for word in words:
    frequency = unique_words.get(word, 0)
    unique_words[word] = frequency + 1
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

words = list(unique_words.keys())
words = list(word_to_count.keys())
words.sort()


max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, unique_words[word]))
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))
