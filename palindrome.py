usrinput = str(input("Enter some word. I will check if this is a palindrome"
                     + ". Enter your word here: "))

#value1 = len(usrinput)
#str_len = range(0, value1)

if usrinput == usrinput[::-1]:
    print("Your word is a palindrome:")
    print(usrinput)
    print(usrinput[::-1])
else:
    print("Your word is not a palindrome.")
