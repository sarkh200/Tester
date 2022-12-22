from os import name
import random
import os

# A dictionary of the things tested on
testTerms = {
    "Marruá": "Agrale",
    "Luling": "Beijing Automobile Works",
    "T-Rex": "Bremach",
    "Star": "Chang'an",
    "Colorado": "Chevrolet",
    "D-Max": "Chevrolet",
    "LSSV ": "Chevrolet",
    "Silverado": "Chevrolet",
    "Montana": "Chevrolet",
    "Labo": "Damas/Labo",
    "Hijet": "Daihatsu",
    "Rich": "Dongfeng",
    "Fullback": "Fiat",
    "Strada": "Fiat",
    "Toro": "Fiat",
    "Maverick": "Ford",
    "F-150": "Ford",
    "F-250": "Ford",
    "F-350": "Ford",
    "F-450": "Ford",
    "SUP": "Foton",
    "Tunland": "Foton",
    "Canyon": "GMC",
    "Sierra": "GMC",
    "GA200": "Gonow",
    "Deer": "Great Wall",
    "V240": "Great Wall",
    "Wingle 5": "Great Wall",
    "Wingle 6": "Great Wall",
    "Ruiyi": "Hafei",
    "Acty": "Honda",
    "Ridgeline": "Honda",
    "Porter": "Hyundai",
    "Santa Cruz": "Hyundai",
    "Arisun": "Iran Khodro",
    "Bardo": "Iran Khodro",
    "D-Max": "Isuzu",
    "Gladiator": "Jeep",
    "Bongo": "Kia",
    "Scorpio": "Mahindra",
    "BT-50": "Mazda",
    "T60": "Maxus",
    "X-Class": "Mercedes-Benz",
    "Minicab": "Mitsubishi",
    "Triton": "Mitsubishi",
    "Pony": "Namco",
    "Clipper": "Nissan",
    "Frontier": "Nissan",
    "NP200": "Nissan",
    "Navara": "Nissan",
    "Titan": "Nissan",
    "R1T": "Rivian",
    "Hilux": "Toyota",
    "Land Cruiser": "Toyota",
    "Tacoma": "Toyota",
    "Tundra": "Toyota",
}


# gets a list of keys
testKeys = list(testTerms.keys())
# gets a list of values
testValues = list(testTerms.values())


def clr():
    if name == "nt":
        x = "cls"
    else:
        x = "clear"
    return os.system(x)


# clears command prompt
clr()


def main(clear=True, textToPrint=None):
    if clear is True:
        clr()
    if textToPrint is not None:
        print(textToPrint)
    print("Do you want to study or test?")
    while True:
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


def test():
    clr()
    # the variable of randTruckInt will equal the random integer from 0 to the length of the list - 1 because lists go from 0 → ∞ instead of 1 → ∞
    randTruckInt = random.randrange(0, len(testTerms) - 1)
    print("Let's begin")
    print("I'll display the truck model and you'll need to input the brand")
    print("Input 'exit' in order to exit")

    # Loops the commands until the user gets the question right
    while True:
        # prints the value in the list at the random value
        print(testKeys[randTruckInt])
        answer = input(":")
        if answer.lower() == testValues[randTruckInt].lower():
            print("Good job")
            a = input("Do you want to go again?: ")
            if a.lower() == "yes" or a.lower() == "y":
                test()
                break
            main()
        if answer.lower() == "exit":
            main(True, "Exited Test")
        else:
            clr()
            print("Incorrect, try again")
            print("I'll display the truck model and you'll need to input the brand")
            print("Input 'exit' in order to exit")


def practice():
    clr()
    print("Let's begin")
    print("I'll display the truck model and you'll need to input the brand")
    # Loops the commands until the user gets the question right
    while True:
        randTruckInt = random.randrange(0, len(testTerms) - 1)
        print("Input 'exit' in order to exit")
        # prints the value in the list at the random value
        print(testKeys[randTruckInt])
        answer = input(":")
        if answer.lower() == testValues[randTruckInt].lower():
            print("Good job")
            a = input("Do you want to go again?: ")
            if a.lower() == "yes" or a.lower() == "y":
                practice()
            # the break command ends the while loop
            break
        if answer.lower() == "exit":
            main(True, "Exited Practice")
        else:
            clr()
            print("Incorrect, the correct answer was: " +
                  testValues[randTruckInt])


def study():
    clr()
    print("View terms: T")
    print("Practice: P")
    a = input(":")
    if a.lower() == "t":
        # prints out the dictionary in Key:Value format
        for key, value in testTerms.items():
            print('%s:%s\n' % (key, value))
        input("Press enter to continue")
        main()
    if a.lower() == "p":
        practice()
    else:
        study()


main(False)
