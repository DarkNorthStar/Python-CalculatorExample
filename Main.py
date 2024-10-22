
import Calculator
import TicTacToe
import Grid
import Vector2D
import time
from Calculator import Calculator

import os
# this is where the calculator will be used for testing and demo

# Main is the entry point of the program
def main():    
    os.system("cls") # Anytime the program runs clear the console
    Continue = True # Variables used to stop the menu loop

    # menu Loop
    while(Continue):
        MenuSelectionValid = False

        # Loop until the user inputs a valid menu selection
        while(MenuSelectionValid == False):
            os.system("cls")
            
            # Print banner
            print("=======================================================\n                     Main Menu\n=======================================================\n")
            #Print Menu options
            MenuSelection  = input("Select a menu Option:\n1. Basic Calculator\n2. TicTacToe\n3. GridDemo\n0. Exit\n")

            # Determine the selection
            if(MenuSelection == "0"):
                Continue = False
                MenuSelectionValid = True
            elif(MenuSelection == '1'):
                # Start basic calculator loop
                Calculator.StartCalculator()
            elif(MenuSelection == '2'):
                TicTacToe.StartGame()
            elif(MenuSelection == '3'):
                
                ContinueGridDemo = True

                grid = Grid(10, 10, 10, 10)


                while(ContinueGridDemo):
                    print("Location:" + grid.GetCurrentLocation().ToString() + "        Distance Traveled:" + grid.GetDistanceTraveled())
                    
                    inputValid = False
                    while(not inputValid):
                        inputToValidate  = input("Enter w,a,s or d to move one space the relative direction").lower()

                        if(inputToValidate in ["w","a","s","d"]):
                            inputValid = True
                            if(inputToValidate == "w"):
                                grid.Move(Vector2D(0,1))
                            elif(inputToValidate == "a"):
                                grid.Move(Vector2D(-1,0))
                            elif(inputToValidate == "s"):
                                grid.Move(Vector2D(0,-1))
                            elif(inputToValidate == "d"):
                                grid.Move(Vector2D(1,0))
                        else:
                            os.system("cls")
                            print("Invalid Entry! Try Again")
            else:
                # Clear the console and output error before retrying
                os.system("cls")
                print("invalid Menu Selection\n")

        

if __name__ == "__main__":
    main()