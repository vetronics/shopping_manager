# import ascii art module graph and plot module and pandas 
import pyfiglet
import os
import matplotlib.pyplot as plt
import pandas as pd 
import pyautogui

# setup windows shell
os.system("cls")
os.system("title shopping manager")
os.system("color 03")

# use pyfiglet module to use ascii art in the shell
result = pyfiglet.figlet_format("shopping manager", font="bulbhead")
print(result)

'''  i define all
procedure under
this rows'''

def elements_counting():
    print("element counting")
    try:
        # open two files measure length and counting elements and values in the file 
        with open("shopping_manger_items_list.csv", "r") as file:
            lines = file.readlines()
            elements = len(lines)
            print("there are total in first file:", elements)

        with open("shopping_manger_items_value.csv", "r") as file:
            lines = file.readlines()
            value_elements = len(lines)
            print("there are total in the second file:", value_elements)

    except FileNotFoundError:
        print("file not found ")

def add_item():
    with open("shopping_manger_items_list.csv", "a") as file:
        elements.append(element_added)
        file.write(element_added + "\n")

def remove_items():
    # open file and wipe out all items in file 
    with open("shopping_manger_items_list.csv", "w") as file:
        elements.remove(element_removed)
        file.write(element_removed)

def add_value():
    with open("shopping_manger_items_value.csv", "a") as file:
        value_elements.append(element_value)
        file.write(str(element_value) + "\n")

def remove_values():
    # open file and wipe out all values in file 
    with open("shopping_manger_items_value.csv", "w") as file:
        value_elements.remove(element_value)
        file.write(str(element_value))

def sum_value_procedure():
    # read file csv 
    df_value = pd.read_csv("shopping_manger_items_value.csv", header=None)

    # sum values in dataframe
    print(df_value.sum(numeric_only=True))

def manage_plot():
    try:
        # Read file csv about list items 
        df_list = pd.read_csv("shopping_manger_items_list.csv", names=["list"], header=None)
        df_list = df_list.dropna()

        # Data visualization in the terminal 
        print("Item list:\n", df_list.values)

        # Read file csv for values
        df_value = pd.read_csv("shopping_manger_items_value.csv", names=["price"], header=None)
        df_value = df_value.dropna()

        # Data visualization in the terminal 
        print("Item prices:\n", df_value.values)

        # Merge the data from two csv files
        labels = df_list['list'][:len(df_value)]  # Ensure same length

        # Set up plot with labels
        df_value['price'].plot(kind='pie', labels=labels, title='Shopping Manager')

        plt.show()

    # Error control      
    except FileNotFoundError:
        print("error file load \n")
   
    except KeyError:
        print("error in pandas series ")
        
    except TypeError:
        print("there are no data in file ")

# to declare variables and dynamic array
elements = []
value_elements = []

# main loop 
while True:
    options = [
        "1) add items", 
        "2) remove items", 
        "3) add value", 
        "4) remove values", 
        "5) element counting", 
        "6) sum of values", 
        "7) data visualization", 
        "8) exit "
    ]

    print("you are welcome shopping manager\n\n")
    print("what do you wanna do? insert your option\n\n")

    for option in options:
        print(option)

    try:
        # choice menu
        choice = int(input())

        if choice == 1:
            print("insert items you want to add")
            element_added = input()
            add_item()

        elif choice == 2:
            print("it is removing whole file data")
            element_removed = input()
            if element_removed == "wipe out all":
                remove_items()

        elif choice == 3:
            print("insert the value number of shop")
            element_value = input()
            add_value()

        elif choice == 4:
            print("it is removing whole file data")
            element_value = input()
            if element_value == "wipe out all":
                remove_values()

        elif choice == 5:
            elements_counting()

        elif choice == 6:
            sum_value_procedure()

        elif choice == 7:
            manage_plot()

        elif choice == 8:
            
            pyautogui.alert(text='you are exiting from shopping manager', title='alert', button='OK')

            break

    except ValueError:
        print("you should verify input \n\n")
