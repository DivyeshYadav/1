varT = True
sublist = []
phonebook = []

while varT:
    print()
    print("               WELCOME TO THE PHONEBOOK                                      ")
    print("#"*45)
    print("               PLEASE CHOOSE THE OPTION BELOW                                                              ")
    print()
    print("A - Add Contact")
    print("S - To search a contact")
    print("E - To exit phonebook")

    option = input("Please Enter Your opinion")

    if option == "E":
        varT = "False"
        print("Thank you for using the phonebook,See you again")

    elif option == "A":
        name = input("Please enter a name")
        number = input("Please enter a number")
        email = input("Pease enter a email id")

        sublist = [name,number,email]
        phonebook.append(sublist)

        print("The contact {} has been added sucessfully!".format(name))

    elif option == "S":
        sname = input("Please enter name to search")
        found = False
        
        for sublist in phonebook:
            if sname in sublist:
                print("{} is found in the phonebook and here are the details".format(sname))
                print(sublist)

                fond = True

        if not found:
            print("{} is not found in the phonebook".format(sname)) 

    else:
        print("Sorry you have chosen the wrong option, Please Try again!")
