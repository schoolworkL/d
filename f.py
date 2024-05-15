# Created by: Landon Walker
# 14/5/2024
# Student Program
# Version = '0.1'
# Program Description: User searches for a last name, full name and phone number are displayed

# sorts a 2D list alphabetically by index 1.
# @param data - holds the 2D list of values
# @return - returns the sorted data from the text file
def sorter(data):
    for i in range(len(data) - 1, 0, -1):  # iterates through the list
        value = 0  # sets value to 0
        # counter = i - 1
        for j in range(1, i + 1):  # iterates through the list between 1 and i + 1
            if data[j][1] > data[value][1]:  # checks if the second value is greater than first value
                value = j  # sets value to j
        data[i], data[value] = data[value], data[i]  # swaps the values of data[i] and data[value]
    return data  # returns the sorted list to the main


# Reads a text files and saves the data as a 2D list
# @return - returns the data from the text file
def read_in():
    with open(
            "C:\\Users\\walkerl407\\Downloads\\Friends Phone List2.txt") as f:  # sets f as the variable to open the text file
        data = f.read().splitlines()  # data holds the lines in the text file as a 2D list
        data = [i.split() for i in data]  # each index is separated into first name, last name, and phone number
        return data  # the text file data is returned to the main


# takes an input to search for in the list of names
# @param data - the list of sorted data
# @return - returns the result of the search to the run(info) function
def search():
    while True:
        try:
            name = str(input("\nSearch by Last Name: "))  # takes a name input to search for
            return Friend.binary_search(0, len(info) - 1,
                                        name)  # returns the result of the search to the run(info) function
        except:
            print("Invalid Input!")  # error message


# checks if a result was found, then displays an output
# @param data - holds the list of sorted data
# @param num - holds the result from the search
def end_result(data, num):
    if num == -1:  # checks if no result was found
        print("\nName not Found!")  # display no value found
    else:
        print(
            f"\nFirst Name: {data[num][0]}\nLast Name: {data[num][1]}\nPhone Number: {data[num][2]}")  # displays
        # results


# stores the result of the search, then runs the function to display the result
# @param info - holds the list of sorted data
def run(info):
    while True:
        result = search()
        end_result(info, result)


# holds the search functionality of the program
class Friend:
    global info  # allows the class to access the sorted list of data
    lst = info  # sets the list of data to be a variable in the class

    # recursive binary search algorithm
    # @param lst - holds the sorted list of data
    # @param low - holds the start value of the list
    # @param high - holds the end value of the list
    # @param term - stores the value of the search term
    # @return mid - returns the mid to the search(data) function
    # @return return Friend.binary_search(lst, low, mid - 1, term) - returns the binary search function with a new high
    # @return Friend.binary_search(lst, mid + 1, high, term) - returns the binary search function with a new low
    # @return -1 - returns value of -1 to the search(data) function
    def binary_search(low, high, term):
        if high >= low:  # checks if the upper range of the list is greater than the lower range of the list
            mid = (high + low) // 2  # stores the index value of the middle value
            if str(Friend.lst[mid][
                       1].casefold()) == term.casefold():  # checks if the middle value is equal to the search term
                return mid  # returns the mid index to the search(data) function
            elif str(Friend.lst[mid][1].casefold()) > term.casefold():  # checks if the middle value is greater than the
                # search term
                return Friend.binary_search(low, mid - 1, term)  # returns the binary search function with a new
                # upper bound
            else:
                return Friend.binary_search(mid + 1, high, term)  # returns the binary_search function with a
                # new lower bound
        else:
            return -1  # returns a value of -1 to indicate no value found


info = read_in()  # stores the data from the text file
sorter(info)  # sorts the data in the info variable
print(info)  # displays info
run(info)  # the function that loops through searching and displaying a result
