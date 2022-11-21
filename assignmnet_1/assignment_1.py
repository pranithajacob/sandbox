
"""
Name: Pranitha balusu
Brief Project Description:
GitHub URL:
"""

from operator import itemgetter, le
from datetime import date
import csv


menu_list = ("\nMenu: ""\nD - dispaly movies \nA - Add new movie \nW - watch a movie  \nQ - Quit\n>>>")   #string for menu

title = 0
year = 1
category = 2
marked = 3

CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Thriller"]


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
            watched_place_number = watched_movie_number + 1
            movie = line.strip().split(",")
            watched_list.append(movie)
        else:
            movie = line.strip().split(",")
            unwatched_list.append(movie)
    # converting priority from string to int
    for i in range(0, len(unwatched_list)):
        (unwatched_list) = (unwatched_list)
    for i in range(0, len(watched_list)):
        (watched_list) = (watched_list)
    print(number_of_lines, "places loaded from movies.csv")
    print("@@@@@ ", watched_list )
    print("### ", unwatched_list)
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
    unwatched_list = sorting_unwatched(watched_list,unwatched_list)
    watched_list = sorting_watched(watched_list, unwatched_list)
    user_input = input(menu_list).lower()
    while user_input not in error_check:  # error checking for other user inputs
        user_input = input("Invalid Menu choice" + menu_list)
    # calling function according to user input
    if user_input == "d":
        movie_list(watched_list, unwatched_list)
        menu_page(watched_list, unwatched_list)
    elif user_input == "a":
        adding_error_check(watched_list, unwatched_list)  # calling adding error function
    elif user_input == "w":
        mark_place(watched_list, unwatched_list)  # calling mark place function
    elif user_input == "q":
        for i in range(0, (len(watched_list))):
            unwatched_list.append(watched_list[i])  # combining both  visited and unvisited list
        print(str(len(unwatched_list)) + " movies saved to movies.csv \nHave a nice day :)")
        quit()


# function for list of places
def movie_list(watched_list, unwatched_list):
    unvisited_list = sorting_unwatched(watched_list, unwatched_list)  # calling sorting function
    visited_list = sorting_watched(watched_list, unwatched_list)  # calling sorting function
    for i in range(0, len(unwatched_list)):
        print("*{:<6} {:<12} {:>12} {:>12}".format(str(i+1), str(unwatched_list[i][0]), str(unwatched_list[i][1]), str(unwatched_list[i][2])))
    k = (len(unwatched_list))
    for j in range(0, len(watched_list)):
        print(" {:<6} {:<12} {:>12} {:>12}".format(str(k+1+j), str(watched_list[j][0]), str(watched_list[j][1]), str(watched_list[j][2])))
    title = cat = ""
    year = 0
    while len(title) <= 0:
        title = input("Title:")
        if len(title) <= 0:
            print("Input can not be blank")
    while year <= 0:
        year = int(input("Year:"))
        if year <= 0:
            print("Number must be >= 1")
    print("Categories available: ", CATEGORIES)
    cat = input("Category:")
    if len(cat) <= 0 or cat not in CATEGORIES:
        print("Invalid category; using Other")
        cat = "Other"
    # checking for repetition
    for m in range(0, len(temp_list)):
        if (temp_list[m][0]).lower() == title.lower():
            print("Already entered")
            menu_page(watched_list, unwatched_list)  #calling menu page function
    adding_movie(watched_list, unwatched_list, [title, year, cat, 'u'])#calling adding function


# function to add new place
def adding_movie(watched_list, unwatched_list, new_movie):
    with open("movies.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow(new_movie)
        file.close()
    unwatched_list.append(new_movie)
    menu_page(watched_list, unwatched_list)#calling menu page function



# function to mark place
def mark_place(watched_list, unwatched_list):
    if len(unwatched_list) == 0:#checking for number of unvisited place
        print("No unvisited place")

    else:
        movie_list(watched_list, unwatched_list)
        mark_input = (input("Enter the number of a place to be marked as visited: "))
        mark_input = blank_input(mark_input, "Place number")#calling blank input function
        mark_input = numerical_input(mark_input, "marking", watched_list, unwatched_list)#calling numerical input function

        print("    marked input: ", mark_input)

        if mark_input <= len(unwatched_list):#checking if input already visited
            mark_input = mark_input-1
            movie = unwatched_list.pop(mark_input)
            movie[3] = "w"
            watched_list.append(movie)
            # write to csv file
            with open("movies.csv", 'w') as file:
                writer = csv.writer(file)
                for u in unwatched_list:
                    writer.writerow(u)
                for w in watched_list:
                    writer.writerow(w)
                file.close()
        else:
            print("No more movies to watch")
    menu_page(watched_list, unwatched_list) #calling menu page function


main()
