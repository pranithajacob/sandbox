from kivy.app import App

"""
Name: Pranitha balusu
Brief Project Description:
GitHub URL:
"""


from operator import itemgetter
import csv
from movie import movie
menu_list = ("\nMenu: ""\nD - dispaly movies \nA - Add new movie \nW - watch a movie  \nQ - Quit\n>>>")   #string for menu

title = 0
year = 1
category = 2
marked = 3



CATEGORIES = ['action', 'comedy', 'documentary', 'drama', 'thriller']


def main():
    temp_file = []    # temporary file for initial diversion
    watched_list = []    # list of watched places
    unwatched_list = []  # list of unwatched places
    print("Movies to watch 1.0 - by Pranitha balusu")
    number_of_lines = 0
    watched_movie_number = 0
    temp_file = open("movies.csv", "r")  # opening csv file
    # dividing list to watched and unwatched lists
    for line in temp_file:
        number_of_lines = number_of_lines + 1
        if "w" in line:
            watched_movie_number = watched_movie_number + 1
            movie = line.strip().split(",")
            watched_list.append(movie)
        else:
            movie = line.strip().split(",")
            unwatched_list.append(movie)
    # converting priority from string to int
    for i in range(0, len(unwatched_list)):
        (unwatched_list[i][2]) = (unwatched_list[i][2])
    for i in range(0, len(watched_list)):
        (watched_list[i][2]) = (watched_list[i][2])
    print(number_of_lines, "movies loaded from movies.csv")
    menu_page(watched_list, unwatched_list)  # calling menu page function
    temp_file.close()


# function for sorting unvisited list
def sorting_unwatched(watched_list, unwatched_list):
    sorted_list = sorted(unwatched_list, key=itemgetter(2))   # sorts list according to priority
    unwatched_list = sorted_list
    return (sorted_list)


# function for sorting visited list
def sorting_watched(watched_list, unwatched_list):
    sorted_list = sorted(watched_list, key=itemgetter(2))  # sorts list according to priority
    watched_list = sorted_list
    return (sorted_list)


# function for menu page
def menu_page(watched_list, unwatched_list):

    error_check = ["d", "a", "w", "q"]   # list of possible input
    unwatched_list = sorting_unwatched(watched_list, unwatched_list)
    watched_list = sorting_watched(watched_list, unwatched_list)
    user_input = input(menu_list).lower()
    while user_input not in error_check:  # error checking for other user inputs
        user_input = input("Invalid Menu choice" + menu_list)
    # calling function according to user input
    if user_input == "d":
        menu_page(watched_list, unwatched_list)
    elif user_input == "a":
        adding_error_check(watched_list, unwatched_list)  # calling adding error function
    elif user_input == "w":
        mark_place(watched_list, unwatched_list)  # calling mark place function

    else:

        for i in range(0, (len(watched_list))):
            unwatched_list.append(watched_list[i])  # combining both  visited and unvisited list
        print(str(len(unwatched_list)) + " movies saved to movies.csv \nHave a nice day :). ")
        # opening and writing new list to csv file
    with open('movies.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(unwatched_list)
    quit()


# function for list of places
def movie_list(watched_list, unwatched_list):
    unvisited_list = sorting_unwatched(watched_list, unwatched_list)  # calling sorting function
    visited_list = sorting_watched(watched_list, unwatched_list)  # calling sorting function
    for i in range(0, len(unwatched_list)):
        print("*{:<6} {:<12}in {:<12} priority {:>12}".format(str(i+1), str(unwatched_list[i][0]), str(unwatched_list[i][1]), str(unwatched_list[i][2])))
    k = (len(unwatched_list))
    for j in range(0, len(watched_list)):
        print(" {:<6} {:<12}in {:<12} priority {:>12}".format(str(k+1+j), str(watched_list[j][0]), str(watched_list[j][1]), str(watched_list[j][2])))
    print(str(len(watched_list)+len(unwatched_list)) + "places.", end=" ")
    if len(unwatched_list) == 0:
        print("No places left to visit. Why not add a new place?")
    else:
        print("You still want to visit " + str(len(unwatched_list))+"places")


# error checking function for blank input
def blank_input(user_input, input_definition):
    while len(user_input) == 0:
        user_input = input("Input cannot be blank \n" + input_definition)
    return user_input


# error checking function for numerical inputs
def numerical_input(user_input, function_name, watched_list, unwatched_list):
    while user_input.isalpha() or ((int(user_input)) <= 0) or (int(user_input) > (len(watched_list) + len(unwatched_list)) and function_name =="marking"):
        if user_input.isalpha():
            user_input = input("Invalid input; enter a valid number \n>>>")
        elif int(user_input) <= 0:
            user_input = input("Number must be > 0 \n>>>")
        elif (function_name == "marking") and (int(user_input) > (len(watched_list) + len(unwatched_list))):
            user_input = input("Invalid place number \n>>>")
    return int(user_input)


# function to check repetition
def adding_error_check(watched_list, unwatched_list):
    temp_list = []
    for i in range(0, ((len(watched_list)))):  # combining visited and unvisited list to temporary list
        temp_list.append(watched_list[i])
    i = 0
    for i in range(0, ((len(unwatched_list)))):
        temp_list.append(unwatched_list[i])
    new_movie = input("Name:")
    new_movie = blank_input(new_movie, "Name:")
    # checking for repetition
    for m in range(0, len(temp_list)):
        if (temp_list[m][0]).lower() == new_movie.lower():
            print("Already entered")
            menu_page(watched_list, unwatched_list)  #calling menu page function
    adding_movie(watched_list, unwatched_list, new_movie)#calling adding function


# function to add new place
def adding_movie(watched_list, unwatched_list, new_movie):
    temp_addition = []
    temp_addition.append(new_movie)
    new_country = input("Country: ")
    new_country = blank_input(new_country, "Country: ") #calling blank input function
    temp_addition.append(new_country)
    new_priority = (input("Priority: "))
    new_priority = blank_input(new_priority, "Priority") #calling blank input function
    new_priority = numerical_input(new_priority, "adding", watched_list, unwatched_list) #calling numerical input function
    temp_addition.append(new_priority)
    temp_addition.append("n")
    print(temp_addition[0] + " in " + temp_addition[1] + " (priority " + str(
        temp_addition[2]) + ") added to movies to watch")
    unwatched_list.append(temp_addition)#adding new place to unvisited list
    menu_page(watched_list, unwatched_list)#calling menu page function



# function to mark place
def mark_watched(watched_list, unwatched_list):
    if len(unwatched_list) == 0:#checking for number of unvisited place
        print("No unvisited place")

    else:
        movie_list(watched_list, unwatched_list)
        mark_input = (input("Enter the number of a place to be marked as visited"))
        mark_input = blank_input(mark_input, "Place number")#calling blank input function
        mark_input = numerical_input(mark_input, "marking", watched_list, unwatched_list)#calling numerical input function

        if mark_input <= len(unwatched_list):#checking if input already visited
            mark_input = mark_input-1
            (unwatched_list[mark_input][3]) = "v"
            print(unwatched_list[mark_input][0]+" in "+unwatched_list[mark_input][1] + " visited!")
            watched_list.append(unwatched_list.pop(mark_input))

        else:
            print("already marked")
    menu_page(watched_list, unwatched_list) #calling menu page function


def run_test():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")
    default_movie = Movie()
    print(default_movie)
    assert default_movie.title == ""
    assert default_movie.category == ""
    assert default_movie.year == 0
    assert not default_movie.is_watched

    # Test initial-value movie
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", True)
    # TODO: Write tests to show this initialisation works

    # TODO: Add more tests, as appropriate, for each method

def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection)
    assert not movie_collection.movies  # an empty list is considered False

    # Test loading movies
    print("Test loading movies:")
    movie_collection.load_movies('movies.csv')
    print(movie_collection)
    assert movie_collection.movies  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Movie with values
    print("Test adding new movie:")
    movie_collection.add_movie(Movie("Amazing Grace", 2006, "Drama", False))
    print(movie_collection)

    # Test sorting movies
    print("Test sorting - year:")
    movie_collection.sort("year")
    print(movie_collection)
    # TODO: Add more sorting tests

    # TODO: Test saving movies (check CSV file manually to see results)

    # TODO: Add more tests, as appropriate, for each method


run_test()
run_tests()
main()
