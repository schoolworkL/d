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
    with open("C:\\Users\\walkerl407\\Downloads\\Friends Phone List2.txt") as f:  # sets f as the variable to open the text file
        data = f.read().splitlines()  # data holds the lines in the text file as a 2D list
        data = [i.split() for i in data]  # each index is separated into first name, last name, and phone number
        return data  # the text file data is returned to the main


# takes an input to search for in the list of names
# @param data - the list of sorted data
# @return - returns the result of the search to the run(info) function
def search(data):
    while True:
        try:
            name = str(input("\nSearch by Last Name: "))  # takes a name input to search for
            return Friend.binary_search(data, 0, len(info) - 1, name)  # returns the result of the search to the run(info) function
        except:
            print("Invalid Input!")  # error message


# checks if a result was found, then displays an output
# @param data - holds the list of sorted data
# @param num - holds the result from the search
def end_result(data, num):
    if num == -1:  # checks if no result was found
        print("\nName not Found!")
    else:
        print(f"\nFirst Name: {data[num][0]}\nLast Name: {data[num][1]}\nPhone Number: {data[num][2]}")  # displays result


def run(info):
    while True:
        result = search(info)
        end_result(info, result)


class Friend:
    def binary_search(lst, low, high, term):
        if high >= low:
            mid = (high + low) // 2
            if str(lst[mid][1].casefold()) == term.casefold():
                return mid
            elif str(info[mid][1].casefold()) > term.casefold():
                return Friend.binary_search(lst, low, mid - 1, term)
            else:
                return Friend.binary_search(lst, mid + 1, high, term)
        else:
            return -1


info = read_in()
sorter(info)
print(info)
run(info)
