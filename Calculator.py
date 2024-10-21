
import os # Used to clear the screen


 

# Calculator class example for scott

# A class is a representation of something in this case a calculator
# the class defines what a calculator is but isn't really anything until its created at runtime
# then its called object this is object oriented programming OOP
class Calculator:
    
    # Variables
    # Variables are usually declared at the top but fuck you python its best practice but not important in python

    #init function (This is just a constructor fuck you python)
    # A constructor is called when you create the object from the class
    def __init__(self):# fuck you colon
        print("...") # Dont really want to do anything rn here but python wont allow for empty functions

    # this is a function it gets a numeric value from the user
    # Gets a numeric value from the user will continue to ask until satisfied
    # Returns a numeric value 
    def GetNumericValue():
        '''
            This is how functions should be commented in python
            but most other languages do it above the function declaration instead of under

            The comment should contain:
            What the function does
            descriptions of any parameters if any it take and
            description of what the function returns if any
            Sometimes how the function is to be used
        '''

        # local variables
        # local variables are only in the function they are created and are destroyed when the function is completed 
        validInput = False
        
        # Loop until we get valid input
        while(validInput == False):
            value = input("Enter a numeric value\n") # Get input from the user
            
            # Check if the value from the user is numeric
            if(value.isnumeric()):
                # The value from the user is numeric
                validInput = True # Set validInput to true as we have valid input from the user
            else:
                # The value from the user is not numeric
                print(value + " Is not NUMERIC!!!\n") # Output Error Message

        return int(value) # converts to int python hides all the value types and decides what it thinks best but i want this to be a int (a number) so we can do numeric stuff

        
    # This is the start function it will be called in a main program to init the
    # calculators loop    
    def StartCalculator():

        # Clear terminal
        os.system('cls')

        # Init continue bool 
        Continue = True # Used to exit calculator loop

        # Loops until the user decides to exit
        while(Continue):
            
            # Each time the Calculator loop iterates the OperatorValid variable will be set to False
            OperatorValid = False # Init OperatorValid Flag to false as it is not valid by default and will changed to valid when a valid operator is received from the user

            # Operator input loop
            # Loops until the user inputs a valid operator value 0-4
            while(not OperatorValid):
                # Prompt the user for a operator and capture the input in Operator
                Operator = input("Calculator Menu:\n===================================\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n0. Exit\n")

                # Check if the the users input is a valid operator
                if(Operator in ["0","1","2","3","4"]):
                    # The Operator given by the user is valid
                    OperatorValid = True # set OperatorValid true to exit the input loop
                else:
                    # The Operator given by the user is not valid
                    os.system('cls') # Clear terminal
                    print(Operator + " is not a valid option\n") # Output to the user the input given is not valid

                # Check if the user wants to exit the calculator
                if(Operator == 0):
                    # The user wants to exit the calculator
                    Continue = False # Set Continue to False to exit the Calculator loop
                else:
                    # The User wants to complete a operation
                    # Clear terminal
                    os.system('cls')

                    # Get the values to calculate from the user
                    # This is done with functions as its duplicate functionality
                    # this way the code only exists once this has many benefits and should be done like this for best practice
                    FirstValue = Calculator.__GetNumericValue() # Get the first numeric value from user
                    os.system('cls') # Clear terminal
                    SecondValue = Calculator.__GetNumericValue() # Get the second numeric value from user

                    os.system("cls")# Clear terminal

                    # Output based on what operator was selected
                    if(Operator == "1"):
                        print(str(FirstValue) + " + " + str(SecondValue) + " = " + str(FirstValue+SecondValue))
                    elif(Operator == "2"):
                        print(str(FirstValue) + " - " + str(SecondValue) + " = " + str(FirstValue-SecondValue))
                    elif(Operator == "3"):
                        print(str(FirstValue) + " * " + str(SecondValue) + " = " + str(FirstValue*SecondValue))
                    elif(Operator == "4"):
                        print(str(FirstValue) + " / " + str(SecondValue) + " = " + str(FirstValue/SecondValue))
                    
                    # This just stops the program until the user hits okay
                    input("\nEnter anything to continue...")

                    os.system("cls")# Clear terminal and restart loop
