from os import name
import random
import os
import csv
import json

hs = float()
testHeader1 = str()
testHeader2 = str()
testTerms = dict()


def startTests():
    try:
        open("TestTerms.csv")
    except:
        print("Error, Test Terms.csv is corrupted or missing")
        print("Create a new file named 'TestTerms.csv' and input the test data into it (the first row will be treated as the titles for their specific columns)")
        print("Press enter to close terminal")
        input(":")
        quit()
    try:
        open("Config.json")
    except:
        print("Error, Config.json is corrupted or missing")
        print("Please redownload the 'Config.json' file")
        print("Press enter to close terminal")
        input(":")
        quit()
    try:
        with open("Config.json", "r") as configJson:
            config = json.load(configJson)
        hs = config["High Score"]
    except:
        print("Error, Config.json is missing the 'High Score' object")
        print("Please redownload the 'Config.json' file or add the 'High Score' object in the 'Config.json' file")
        print("Press enter to close terminal")
        input(":")
        quit()
    try:
        hs = float(hs)
    except:
        print("Error the 'High Score' object in 'Config.json' is not a number")
        print("Please redownload the 'Config.json' file or edit the 'High Score' object in the 'Config.json' file to equal a number")
        print("Press enter to close terminal")
        input(":")
        quit()


startTests()

with open("Config.json", "r") as configJson:
    config = json.load(configJson)
hs = float(config["High Score"])

data = csv.reader(open('TestTerms.csv', 'r'))  # refrences the csv file

testTerms = {
    rows[0]: rows[1] for rows in data
}  # Generates a test dictionary from the csv file

testHeader1 = list(testTerms.keys())[0]  # gets the header of the
testHeader2 = list(testTerms.values())[0]

# Remove headers from dictionary
testTerms.pop(list(testTerms.keys())[0])


def clr():  # clears the console with cls being used if the user is using an nt kernel
    if name == "nt":
        x = "cls"
    else:
        x = "clear"
    return os.system(x)


clr()  # clears command prompt


def mainMenu(clear=True, textToPrint=None):  # the main menu of the program
    if clear == True:
        clr()
    if textToPrint != None:
        print(textToPrint)

    print("Do you want to study or test?")

    while True:  # loops until user inputs accepted input
        print("Input 'exit' in order to exit")
        a = input(":")
        if a.lower() == "study" or a.lower() == "s":
            study()
            break
        if a.lower() == "test" or a.lower() == "t":
            test()
            break
        if a.lower() == "exit" or a.lower == "e":
            quit()
        clr()
        print("Error, enter 'Study' or 'Test'")


def shuffleDict(refrenceDict):  # returns a shuffled version of a dictionary
    d = {}
    l = list(testTerms.keys())
    random.shuffle(l)
    for key in l:
        d.update({key: refrenceDict[key]})
    return d


class nthDictionary:
    def key(dict=dict(), n=0):  # returns the nth key of a dictionary
        a = str(list(dict.keys())[n])
        return a

    def value(dict=dict(), n=0):  # returns the nth value of a dictionary
        a = str(list(dict.values())[n])
        return a


def test():  # tests the user on the questions
    clr()

    testTerms_shuffled = shuffleDict(testTerms)

    print("Let's begin")

    n = 0
    c = 0

    while n < len(testTerms_shuffled):  # loops until the user goes through all the questions
        print("I'll display the " + testHeader1 +
              " and you'll need to input the " + testHeader2)
        print("Input 'exit' in order to exit")

        q = nthDictionary.key(testTerms_shuffled, n)
        ans = nthDictionary.value(testTerms_shuffled, n)

        print(q)
        answer = input(":")

        if answer.lower() == ans.lower():
            n += 1
            c += 1
            clr()
            print("Good job")

        elif answer == "exit":
            if (((c+1)/(n+1))*100) > float(hs) and n > 0:
                with open('Config.json', 'r+') as configJson:
                    j = json.load(configJson)
                    configJson.seek(0)
                    j["High Score"] = ((c/n)*100)
                    json.dump(j, configJson)
                    configJson.truncate()
            if n > 0:
                mainMenu(True, "Exited Test with a score of: " +
                         str((c/n)*100) + "%")
            else:
                mainMenu(True, "Exited Test with a score of: " +
                         str((c/n+1)*100) + "%")
            break

        else:
            clr()
            print("Incorrect")
            n += 1

    if (((c)/(n))*100) > float(hs) and n > 0:
        with open('Config.json', 'r+') as configJson:
            j = json.load(configJson)
            configJson.seek(0)
            j["High Score"] = (((c)/(n+1))*100)
            print(j)
            json.dump(j, configJson)
            configJson.truncate()

    print("You have tested all of the terms")
    print("You got a score of: " + str(((c+1)/(n+1))*100) + "%")
    print("Would you like to try again?")
    a = input(":").lower()
    if a == "y" or a == "yes":
        test()
    else:
        mainMenu()


def practice():
    clr()

    testTerms_shuffled = shuffleDict(testTerms)

    print("Let's begin")

    n = 0
    c = 0

    while n < len(testTerms_shuffled):
        print("I'll display the " + testHeader1 +
              " and you'll need to input the " + testHeader2)
        print("Input 'exit' in order to exit or 'give up' to go to the next question")

        q = nthDictionary.key(testTerms_shuffled, n)
        ans = nthDictionary.value(testTerms_shuffled, n)

        print(q)
        answer = input(":")

        if answer.lower() == ans.lower():
            n += 1
            c += 1
            clr()
            print("Good job")
        elif answer == "exit":
            mainMenu(True, "Exited Practice Test with a score of:" +
                     str(c/(n+1)*100) + "%")
            break
        else:
            clr()
            print("Incorrect, the correct answer was: " +
                  ans.capitalize())
            print("You answered: " + answer.capitalize())
            n += 1

    print("You have practiced all of the terms")
    print("You got a score of: " + str(((c)/(n+1))*100) + "%")
    print("Try out Test in order to save a high score")
    print("Would you like to try again?")
    a = input(":").lower()
    if a == "y" or a == "yes":
        practice()
    else:
        mainMenu()


def study():
    clr()

    print("View terms: T")
    print("Practice: P")
    print("Exit: E")
    a = input(":")

    if a.lower() == "t":
        for key, value in testTerms.items():  # prints out the dictionary in Key:Value format
            print('%s:%s\n' % (key, value))
        input("Press enter to continue")
        study()
    elif a.lower() == "p":
        practice()
    elif a.lower() == "e":
        mainMenu()
    else:
        study()


mainMenu()
