# import ascii art module 
import pyfiglet
import os
import matplotlib.pyplot as plt
import pandas as pd 

# setup windows shell
os.system("cls")
os.system("title shopping manager")
os.system("color 05")

# use pyfiglet module to use ascii art in the shell
result = pyfiglet.figlet_format("shopping manager", font="bulbhead")
print(result)

'''  i define all
    procedure under
    this row'''

def elements_counting():
    print("element counting")
    with open("shopping_manger_items_list.txt", "r") as file:
        lines = file.readlines()
        elements = len(lines)
    print("there are total in first file:", elements)

    with open("shopping_manger_items_value.csv", "r") as file:
        lines = file.readlines()
        value_elements = len(lines)
    print("there are total in the second file:", value_elements)

def add_items():
    with open("shopping_manger_items_list.txt", "a") as file:
        elements.append(element_added)
        file.write(element_added + "\n")

def remove_items():
    with open("shopping_manger_items_list.txt", "w") as file:
        elements.remove(element_removed)
        file.write(element_removed)

def add_value():
    with open("shopping_manger_items_value.csv", "a") as file:
        value_elements.append(element_value)
        file.write(str(element_value) + "\n")

def remove_value():
    with open("shopping_manger_items_value.csv", "w") as file:
        value_elements.remove(element_value)
        file.write(str(element_value))

def sum_value_procedure():

   df_value = pd.read_csv("shopping_manger_items_value.csv",header=None)
   
   print(df_value.sum(numeric_only=True))
   


def manage_plot():
    try:
        df_value = pd.read_csv("shopping_manger_items_value.csv",names=["price"],header=None)

        df_value = df_value.dropna()

        print(df_value.values)

        df_value['price'].plot(kind='pie',title='shopping manager')

        plt.show()
         
    except FileNotFoundError :
        print("error file load \n")
   
    except KeyError:
        print("price column not found please insert inside csv file")

    except TypeError :

        print("there are not data in file ")

# to declare variables and dynamic array
elements = []
value_elements = []

# main loop 
while True:
    options = ["1) add items", "2) remove items", "3) add value", "4) remove values", "5) element counting", "6) sum of values", "7) data visualization", "8) exit "]

    print("you are welcome shopping manager\n")
    print("what do you wanna do? insert your option\n")

    for option in options:
        print(option)

    try:
        # choice menu
        choice = int(input())

        if choice == 1:
            print("insert items you want to add")
            element_added = input()
            add_items()

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
                remove_value()

        elif choice == 5:
            elements_counting()

        elif choice == 6:
            sum_value_procedure()

        elif choice == 7:
            manage_plot()

        elif choice == 8:
            print("exit by script")
            break

    except ValueError :
        print("you should verify input \n\n")
        