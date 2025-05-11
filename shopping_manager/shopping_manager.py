# import ascii art module 
import pyfiglet
import os
import matplotlib.pyplot as plt

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

    with open("shopping_manger_items_value.txt", "r") as file:
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
    with open("shopping_manger_items_value.txt", "a") as file:
        value_elements.append(element_value)
        file.write(str(element_value) + "\n")

def remove_value():
    with open("shopping_manger_items_value.txt", "w") as file:
        value_elements.remove(element_value)
        file.write(str(element_value))

def sum_value_procedure():
    with open("shopping_manger_items_value.txt", "r") as file:
        value_elements = file.readlines()
    value_elements = map(float, value_elements)
    sum_values = sum(value_elements)
    print(sum_values) 

def manage_plot():
    with open("shopping_manger_items_list.txt", "r") as file:
        plot_elements = file.readlines()

    lenghet_elements = len(plot_elements)

    with open("shopping_manger_items_value.txt", "r") as file2:
        plot_elements_value = file.readlines()
    lenghet_value_elements = len(plot_elements_value)

    if lenghet_elements == lenghet_value_elements:
        fig, ax = plt.subplots()
        ax.set_title('shopping manager')
        plt.xlabel("elements")
        plt.ylabel("price")
        plt.grid(True)
        plt.plot(plot_elements, plot_elements_value)
        plt.show()
    else:
        print("you should verify that the list must be equal\n")

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
        print("you should verify input")
