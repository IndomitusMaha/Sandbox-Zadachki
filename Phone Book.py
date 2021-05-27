Telefonnaya_kniga = {
    'Mukagali' : "+77012088044",
    'Rinad' : "+77025516646",
    'Kanat' : "+77752601300"}

def book():
    for i in Telefonnaya_kniga:
        print(i+" "+Telefonnaya_kniga[i])

def find():
    person = input('Who do you want to find? ')
    found = 1
    for i in Telefonnaya_kniga:
        if person  == i:
            print(i+' '+Telefonnaya_kniga[i])
            found = False
    if found == 1:
        print("Couldn't find this contact")


def add():
    print(" You want to addd person in a book")
    name = input("Name: ")
    number = input("Number: ")
    for i in Telefonnaya_kniga:
        if i == name:
            print("This contact already exsts")
            break
        else:
            Telefonnaya_kniga[name] = str(number)
            print("Contact added")
            book()
            break

def dellete():
    person = input('Who do you want to dellate? ')
    try:
        for i in Telefonnaya_kniga:
            if person == i:
                a = i
        del Telefonnaya_kniga[a]
        print("Contact deleted")
        book()
    except:
        print("No such contact found")

def change():
    who = input('Who\' number do you wnat to change? ')
    newnum = input('New number ')
    try:
        for i in Telefonnaya_kniga:
            if who == i:
                Telefonnaya_kniga[i] = str(newnum)
                break
        print("Changes saved")
        book()
    except:
        print("No such contact found")

def save():
    a = []
    for i in Telefonnaya_kniga:
        a.append(i+' '+Telefonnaya_kniga[i])
    a = str(a)
    TK = open("Phone Book.txt", "w")
    TK.write(a)
    TK.close()
    print("Izmenenya sohraneni")

while True:
    print("\nAvalible commands:\n Book Find Dellete Add Change Save\n")
    action = input("What do you want to do? ")
    if action == 'Book':
        book()
    elif action == 'Find':
        find()
    elif action == 'Dellete':
        dellete()
    elif action == 'Add':
        add()
    elif action == 'Change':
        change()
    elif action == 'Save':
        save()
    else:
        print("There is no such command") 