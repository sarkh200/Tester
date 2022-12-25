import random
import os
import csv
import json

defaultHS = {"High Score": 0}
defaultCSV = {"Question": "Answer",
              "Question1": "Answer1", "Question2": "Answer2"}
hs = float()
testHeader1 = str()
testHeader2 = str()
testTerms = dict()


def startTests():
    try:
        open("TestTerms.csv")
    except:
        print("Error, Test Terms.csv is missing")
        print("A blank csv file will be made on enter")
        print("Input the test data into the csv file (the first row will be treated as the titles for their specific columns)")
        print("Press enter to close terminal")
        input(":")
        with open("TestTerms.csv", "w", newline="") as termsCsv:
            w = csv.writer(termsCsv)
            for x in range(len(defaultCSV)):
                w.writerow([list(defaultCSV.keys())[x],
                           list(defaultCSV.values())[x]])
        quit()
    try:
        data = csv.reader(open("TestTerms.csv", "r"))
        testTerms = {rows[0]: rows[1] for rows in data}
        testHeader1 = list(testTerms.keys())[0]
        testHeader2 = list(testTerms.values())[0]
    except:
        print("Error, Test Terms.csv is corrupted or in an incorrect format")
        print("Press enter to reset the csv file or close the terminal to attempt to fix it yourself")
        print("Input the test data into the csv file (the first row will be treated as the titles for their specific columns)")
        print("Press enter to close terminal")
        input(":")
        with open("TestTerms.csv", "w", newline="") as termsCsv:
            termsCsv.seek(0)
            termsCsv.truncate()
            w = csv.writer(termsCsv)
            w.writerow(["Question", "Answer"])
            w.writerow(["Question1", "Answer1"])
            w.writerow(["Question2", "Answer2"])
        quit()
    try:
        open("Highscore.json")
    except:
        print("Error, Highscore.json is corrupted or missing")
        print("A reset Highscore.json file will be made on enter or exit the program to diagnose the problem yourself")
        print("Press enter to close terminal")
        input(":")
        with open("Highscore.json", "w") as hsJson:
            json.dump(defaultHS, hsJson, indent=4)
        quit()
    try:
        with open("Highscore.json", "r") as configJson:
            config = json.load(configJson)
        hs = config["High Score"]
    except:
        print("Error, Highscore.json is missing the High Score object")
        print("Please redownload the Highscore.json file or add the High Score object in the Highscore.json file")
        print("Press enter to close terminal")
        input(":")
        quit()
    try:
        hs = float(hs)
    except:
        print("Error the High Score object in Highscore.json is not a number")
        print("Please redownload the Highscore.json file or edit the High Score object in the Highscore.json file to equal a number")
        print("Press enter to close terminal")
        input(":")
        quit()


startTests()  # runs tests to check if TestTerms.cs and Highscore.json exists or is configured correctly

with open("Highscore.json", "r") as configJson:
    config = json.load(configJson)
hs = float(config["High Score"])

data = csv.reader(open("TestTerms.csv", "r"))  # refrences the csv file

testTerms = {
    rows[0]: rows[1] for rows in data
}  # Generates a test dictionary from the csv file

testHeader1 = list(testTerms.keys())[0]
testHeader2 = list(testTerms.values())[0]

# Remove headers from dictionary
testTerms.pop(list(testTerms.keys())[0])


def clr():  # clears the console with cls being used if the user is using an nt kernel
    if os.name == "nt":
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
        print("Input exit in order to exit")
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
        print("Error, enter Study or Test")


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

    # loops until the user goes through all the questions
    while n < len(testTerms_shuffled):
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
                with open("Highscore.json", "r+") as configJson:
                    j = json.load(configJson)
                    configJson.seek(0)
                    j["High Score"] = ((c/n)*100)
                    json.dump(j, configJson, indent=4)
                    configJson.truncate()
            if n > 0:
                mainMenu(True, "Exited Test with a score of: " +
                         str((c/n)*100) + "%")
            else:
                mainMenu(True, "Exited Test with a score of: " +
                         str((c/(n+1))*100) + "%")
            break

        else:
            clr()
            print("Incorrect")
            n += 1

    if (((c)/(n))*100) > float(hs) and n > 0:
        with open("Highscore.json", "r+") as configJson:
            j = json.load(configJson)
            configJson.seek(0)
            j["High Score"] = (((c/n))*100)
            json.dump(j, configJson, indent=4)
            configJson.truncate()

    print("You have tested all of the terms")
    print("You got a score of: " + str(((c/n))*100) + "%")
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
        elif answer.lower() == "exit":
            if n > 0:
                mainMenu(True, "Exited Test with a score of: " +
                         str((c/n)*100) + "%")
            else:
                mainMenu(True, "Exited Test with a score of: " +
                         str((c/(n+1))*100) + "%")
            break
        elif answer.lower() == "give up":
            clr()
            print("You inputted 'give up', the correct answer was: " +
                  ans)
            n += 1
        else:
            clr()
            print("Incorrect, try again")
            print("You answered: " + answer.capitalize())

    print("You have practiced all of the terms")
    print("You got a score of: " + str(((c/n))*100) + "%")
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
            print("%s:%s\n" % (key, value))
        input("Press enter to continue")
        study()
    elif a.lower() == "p":
        practice()
    elif a.lower() == "e":
        mainMenu()
    else:
        study()


mainMenu()
