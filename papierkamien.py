import getpass  # Użyty, żeby wybór usr1 nie był widoczny dla usr2. Działa poprawnie tylko w konsoli.  

print("%%%%%%%% PAPIER-KAMIEŃ-NOŻYCE %%%%%%%%")

usr1 = str(input("Pierwszy gracz: "))
usr2 = str(input("Drugi gracz: "))

print("Witajcie " + usr1 + " i " + usr2 + "!" + " Zagrajmy w papier-kamień-nożyce!")

def oneturn():

    print("\n" + usr1 + "! Czas na Twój ruch!")

    ruchusr1 = getpass.getpass(usr1 + "?, Co wybierasz? (p, k, n)? ")
    ruchusr2 = getpass.getpass(usr2 + "?, Co wybierasz? (p, k, n)? ")

    if ruchusr1 == "p" and ruchusr2 == "p":
        print(usr1 + ": Papier")
        print(usr2 + ": Papier")
        print("\nRemis!")
    elif ruchusr1 == "p" and ruchusr2 == "k":
        print(usr1 + ": Papier")
        print(usr2 + ": Kamień")
        print("\n" + usr1 + " wygrywa!")
    elif ruchusr1 == "p" and ruchusr2 == "n":
        print(usr1 + ": Papier")
        print(usr2 + ": Nożyce")
        print("\n" + usr2 + " wygrywa!")
    elif ruchusr1 == "k" and ruchusr2 == "p":
        print(usr1 + ": Kamień")
        print(usr2 + ": Papier")
        print("\n" + usr2 + " wygrywa!")
    elif ruchusr1 == "k" and ruchusr2 == "k":
        print(usr1 + ": Kamień")
        print(usr2 + ": Kamień")
        print("\nRemis!")
    elif ruchusr1 == "k" and ruchusr2 == "n":
        print(usr1 + ": Kamień")
        print(usr2 + ": Nożyce")
        print("\n" + usr2 + " wygrywa!")
    elif ruchusr1 == "n" and ruchusr2 == "p":
        print(usr1 + ": Nożyce")
        print(usr2 + ": Papier")
        print("\n" + usr1 + " wygrywa!")
    elif ruchusr1 == "n" and ruchusr2 == "k":
        print(usr1 + ": Nożyce")
        print(usr2 + ": Kamień")
        print("\n" + usr2 + " wygrywa!")
    elif ruchusr1 == "n" and ruchusr2 == "n":
        print(usr1 + ": Nożyce")
        print(usr2 + ": Nożyce")
        print("\nRemis!")

oneturn()
oneturn()
oneturn()
