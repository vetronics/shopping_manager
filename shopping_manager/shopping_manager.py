# import asci art module 
import pyfiglet
import os

#setup windows shell
os.system("cls")
os.system("title shopping manager")
os.system("color 05")

# use pyfiglet module use asci art in the shell
result = pyfiglet.figlet_format("shopping manager", font="bulbhead")

print(result)
'''  i define  all
    procedure  under
    this row'''

def elements_counting():
    print("element counting")
    file = open("shopping_manger_items_list.txt", "r")
    lines = file.readlines()
    elements = len(lines)
    print("there are total in first file:", elements)
    file.flush()
    file.close()

    file = open("shopping_manger_items_value.txt", "r")
    lines = file.readlines()
    value_elements = len(lines)
    print("there are total in the second file:", value_elements)
    file.flush()
    file.close()

def add_items():
    file = open("shopping_manger_items_list.txt", "a")    
    elements.append(element_added)
    file.write(element_added + "\n")
    file.flush()
    file.close()

def remove_items():
    file = open("shopping_manger_items_list.txt", "w")
    elements.remove(element_removed)
    file.write(element_removed)
    file.flush()
    file.close()

def add_value():
    file = open("shopping_manger_items_value.txt", "a")    
    value_elements.append(element_value)
    file.write(str(element_value + "\n"))
    file.flush()
    file.close()

def remove_value():
    file = open("shopping_manger_items_value.txt", "w")
    value_elements.remove(element_value)
    file.write(str(element_value))
    file.flush()
    file.close()
    
def sum_value_procedure():
    file= open("shopping_manger_items_value.txt", "r")
    value_elements =file.readlines()
    value_elements = map(float,value_elements)
    sum_values =(sum(value_elements))
    print(sum_values)    
    file.flush()
    file.close()
        
    
# to declare variables and dynamic array
elements = []
value_elements = []

# main loop 
while True:
    options = ["1) add items", "2) remove items", "3) add value", "4) remove values", "5) element counting","6) sum of values","7) exit by program"]

    print("you are welcome shopping manager\n")
    print("what do you wanna do? insert your option\n")

    for option in options:
        print(option)

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
        element_value = float(input())
        add_value()

    elif choice == 4:
        print("it is removing whole file data")
        element_value = input()
        if element_value == "wipe out all":
            remove_value()

    elif choice == 5:
        elements_counting()
        
    elif choice == 6 :
        sum_value_procedure()

    elif choice == 7:
        print("exit by script")
        break
