def main():
    # Problem1()
    Problem2()


# Create a function that has a loop that quits with q
# Allow the User to enter names until q is entered
# Add each name entered to a List
# When the User enters q print the list of names
# ADDITIONAL REQUIREMENTS:
# Your code should be able to process the quit command (q) the User enters regardless of case
def Problem1():
    userInput = input("Compile a list of names. Enter q to quit.")
    userInputPrint = ""

    while (userInput != 'q'):
        userInputPrint += userInput + "\n"
        userInput = input("Enter q to quit ")
    print(userInputPrint)


# Create a function that does the following when called:
# Prints a formatted list of names and ages

def Problem2():
    myDictionaryList = [
        {
            "name": "Kelvin",
            "age": 30
        },
        {
            "name": "Bob",
            "age": 50
        },
        {
            "name": "Alex",
            "age": 21
        }
    ]
    for eachEl in myDictionaryList:
        print(eachEl["name"])
        print(eachEl["age"])



 #Prompts the User for which property they want to use to sort the list (e.g. AGE or NAME).
# Print the formatted list of names and ages sorted by the specified sort criteria.
    age = input("Enter age")
    for eachEl in myDictionaryList:
        print(age)
    myDictionaryList=sorted(myDictionaryList)
    print(sorted(myDictionaryList))







if __name__ == '__main__':
    main()
