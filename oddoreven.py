def numcheck():

    numcheckask = int(input("Please provide some number."
                            "\nI will tell you if it's odd or even."
                            "\nType your number here: "))

    if numcheckask % 2 == 0:
        print('This number is even.')
    else:
        print("This number is odd.")

    if numcheckask % 2 == 0:
        if numcheckask % 2 == 0 and numcheckask % 4 == 0:
            print('Also, this number is a multiple of 4.')

    comparison = int(input("Now let's check if "
                           + str(numcheckask)
                           + " can be divided by another number without remainder."
                           +  "\nPlease type your second number: "))

    if numcheckask % comparison == 0:
        print("Yes, the remainder is 0.")
    else:
        print("No, the remainder is " + str(numcheckask % comparison) + ".")

numcheck()