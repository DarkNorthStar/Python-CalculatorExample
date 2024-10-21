
import Calculator
from Calculator import Calculator

import os
# this is where the calculator will be used for testing and demo

# Main is the entry point of the program
def main():

    os.system("cls")

    Continue = True

    while(Continue):
        MenuSelectionValid = False

        while(MenuSelectionValid == False):
            # Print banner
            print("=======================================================\n                     Main Menu\n=======================================================\n")
            #Print Menu options
            MenuSelection  = input("Select a menu Option:\n1. Basic Calculator\n0. Exit\n1")

            # Determine the selection
            if(MenuSelection == "0"):
                Continue = False
            elif(MenuSelection == '1'):
                # Start the calculator
                Calculator.StartCalculator()
            else:
                os.system("cls")
                print("invalid Menu Selection\n")

        

if __name__ == "__main__":
    main()