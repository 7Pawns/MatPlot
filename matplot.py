import matplotlib.pyplot as plt
import re
import numpy as np


"""
The method Calculator lets the user input a mathematical function and it solves it
Then it compares it to the user's guess and inputs both the real answer and the user's
into the matching lists
"""

def Calculator(userAnswers, realAnswers, problemList):
    print("Welcome To My Calculator!")
    continueInput = True; # Should continue taking inputs?
    problemCounter = 0 # How many mathematical functions were written?

    while continueInput:
        continueInputCheck = "-1" # For later use when checking with user

        problem = input("Write your math problem: ")
        # Regex for everything that is a mathematical function
        # Trying to eval the problem after checking it is a function and not malicious code
        # To avoid getting errors in problems like 8/0
        # Not using Try/Except makes the regex much more complex therefore I decided to use it
        # Please forgive me
        while re.search(r"^ *[-+( )*]? *\d+([.]?\d*)?( *[-+/*] *\d+([.]?\d*)?)*$", problem) == None or TryToEvaluate(problem) == None:
            problem = input("Invalid input. Try Again: ")

        user_answer = input("Your guess: ")
        # Regex for ints and floats
        while re.match(r"^[+-]?\d+([.]?\d*)?$", user_answer) == None:
            user_answer = input("Invalid input. Try Again: ")


        evaluatedProblem = eval(problem)
        # Comparing answers
        if eval(user_answer) == evaluatedProblem:
            print("Correct.")
        else:
            print(("Incorrect. The solution is: " + str(evaluatedProblem)))

        problemCounter += 1

        # Adding each answer to the matching list
        # And adding a question number
        problemList.append(problemCounter)
        userAnswers.append(eval(user_answer))
        realAnswers.append(evaluatedProblem)

        # Checking for more inputs from user
        while continueInputCheck not in "01":
            continueInputCheck = input("Do you wish to continue, or get the graph results? "
                                  "0 -> stop  1 -> continue ")
        if continueInputCheck == "0":
            continueInput = False

""" 
Checking that the problem is mathematically possible
"""
def TryToEvaluate(problem):
    try:
        userAnswer = eval(problem)
    except:
        return None
    return userAnswer

# Lists for the plot
userAnswers = []
realAnswers = []
problemList= []

# Calling the method
Calculator(userAnswers, realAnswers, problemList)

# Creating each graph with matching label
plt.plot(problemList, userAnswers, label= "User")
plt.plot(problemList, realAnswers, label= "Calculator")
plt.legend()

# Graph adjustments
plt.xticks(np.array(problemList)) # Intervals between ticks
plt.yscale("linear") # To place the ticks in the Y axis according to math, and not index in array
plt.xlabel('Problem Number')
plt.ylabel('Answer')
plt.title('Calculator vs Human')

# Showing the graph
plt.show()
