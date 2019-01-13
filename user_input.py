def UsrInput():

    name = input("Please enter your name: ")  # type: str
    print("Hello " + name + "! Welcome!")

    age = int(input("Please enter your age: "))
    agediff = 2018 + 100 - age
    print("Thank you, " + name + "! Did you know that you will turn 100 years old in " + str(agediff) + "?")

UsrInput()