#Add function and corresponding code
import PySimpleGUI as sg

def add(): #Add Shortcut, Password, and Usernames to directory
    Shortcut = input("Shortcut: ")
    Usernames = input("Username: ")
    Password = input("Password: ")
    Shortcutwrite(Shortcut)
    Usernameswrite(Usernames)
    Passwordwrite(Password)

def Shortcutwrite(Shortcut): #Write Shortcut in Shorcut.txt
    try:
        Keepdata = [x.strip() for x in open("Shortcuts.txt").readlines()]
        typeShort = open("Shortcuts.txt", "w")
    except:
        typeShort = open("Shortcuts.txt", "w")
        Keepdata = [x.strip() for x in open("Shortcuts.txt").readlines()]
    for Info in Keepdata:
        typeShort.write(str(Info) + "\n")
    typeShort.write(Shortcut + "\n")
    typeShort.close()

def Usernameswrite(Usernames): #Write Usernames in Usernames.txt
    try:
        Keepdata = [x.strip() for x in open("Usernames.txt").readlines()]
        typeUser = open("Usernames.txt", "w")
    except:
        typeUser = open("Usernames.txt", "w")
        Keepdata = [x.strip() for x in open("Usernames.txt").readlines()]
    for Info in Keepdata:
        typeUser.write(str(Info) + "\n")
    typeUser.write(Usernames + "\n")
    typeUser.close()

def Passwordwrite(Password): #Write Password in Passwords.txt
    try:
        Keepdata = [x.strip() for x in open("Passwords.txt").readlines()]
        typePass = open("Passwords.txt", "w")
    except:
        typePass = open("Passwords.txt", "w")
        Keepdata = [x.strip() for x in open("Passwords.txt").readlines()]
    for Info in Keepdata:
        typePass.write(str(Info) + "\n")
    typePass.write(Password + "\n")
    typePass.close()

#Remove function and corresponding code

def remover(): #Remove data from directory
    global Keepdata
    global Keepdata2
    global Keepdata3
    global RemoveIndex
    RemoveIndex = []
    Keepdata = [x.strip() for x in open("Shortcuts.txt").readlines()]
    Keepdata2 = [x.strip() for x in open("Usernames.txt").readlines()]
    Keepdata3 = [x.strip() for x in open("Passwords.txt").readlines()]
    while True:
        Shortcut = input("What is the shortcut?: ")
        if not(Shortcut == ""):
            print("")
            Remover(Shortcut, Keepdata)
            break
        Usernames = input("What is the username?: ")
        if not(Usernames == ""):
            print("")
            Remover(Usernames, Keepdata2)
            break
        Password = input("What is the password?: ")
        if not(Password == ""):
            print("")
            Remover(Password, Keepdata3)
            break
        print("")

def Remover(Value, Data):
    for Info in range(len(Data)):
        if Value == Data[Info]:
            RemoveIndex.append(Info)
    RemoveIndex.reverse()
    for Info in RemoveIndex:
        Keepdata.remove(Keepdata[Info])
        Keepdata2.remove(Keepdata2[Info])
        Keepdata3.remove(Keepdata3[Info])
    typeShort = open("Shortcuts.txt", "w")
    for Info in Keepdata:
        typeShort.write(str(Info) + "\n")
    typeShort.close()
    typeUser = open("Usernames.txt", "w")
    for Info in Keepdata2:
        typeUser.write(str(Info) + "\n")
    typeUser.close()
    typePass = open("Passwords.txt", "w")
    for Info in Keepdata3:
        typePass.write(str(Info) + "\n")
    typePass.close()
    print("Removed " + str(len(RemoveIndex)) + " stored data lines")

#Find function and correspondding code

def find():
    global Keepdata
    global Keepdata2
    global Keepdata3
    Keepdata = [x.strip() for x in open("Shortcuts.txt").readlines()]
    Keepdata2 = [x.strip() for x in open("Usernames.txt").readlines()]
    Keepdata3 = [x.strip() for x in open("Passwords.txt").readlines()]
    while True:
        Shortcut = input("What is the shortcut?: ")
        if not(Shortcut == ""):
            print("")
            Finder(Shortcut, Keepdata)
            break
        Usernames = input("What is the username?: ")
        if not(Usernames == ""):
            print("")
            Finder(Usernames, Keepdata2)
            break
        Password = input("What is the password?: ")
        if not(Password == ""):
            print("")
            Finder(Password, Keepdata3)
            break
        print("")

def Finder(Value, Data):
    print("Shortcut: Username:Password \n")
    for Info in range(len(Data)):
        if Value == Data[Info]:
            print(Keepdata[Info] + ": " + Keepdata2[Info] + ":" + Keepdata3[Info])

#Read function and corresponding code

def read():
    print("")
