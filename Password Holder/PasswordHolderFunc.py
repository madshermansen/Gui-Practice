#Add function and corresponding code
import PySimpleGUI as sg
import PasswordHolderGUI

def add(Shortcut, Usernames, Password): #Add Shortcut, Password, and Usernames to directory
    if Shortcut == "" or Usernames == "" or Password == "":
        print("Please enter values")
        return
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

def remover(Shortcut, Usernames, Password, Testfor): #Remove data from directory
    if Testfor != []:
        Shortcut = Testfor[0]
    elif Shortcut == "" or Usernames == "" or Password == "":
        return
    global Keepdata
    global Keepdata2
    global Keepdata3
    global RemoveIndex
    RemoveIndex = []
    Keepdata = [x.strip() for x in open("Shortcuts.txt").readlines()]
    Keepdata2 = [x.strip() for x in open("Usernames.txt").readlines()]
    Keepdata3 = [x.strip() for x in open("Passwords.txt").readlines()]
    while True:
        if not(Shortcut == ""):
            Remover(Shortcut, Keepdata)
            break
        if not(Usernames == ""):
            Remover(Usernames, Keepdata2)
            break
        if not(Password == ""):
            Remover(Password, Keepdata3)
            break

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

def find(Shortcut, Username, Password):
    if Shortcut == "" or Username == "" or Password == "":
        return
    global Keepdata
    global Keepdata2
    global Keepdata3
    Keepdata = [x.strip() for x in open("Shortcuts.txt").readlines()]
    Keepdata2 = [x.strip() for x in open("Usernames.txt").readlines()]
    Keepdata3 = [x.strip() for x in open("Passwords.txt").readlines()]
    while True:
        if not(Shortcut == ""):
            Finder(Shortcut, Keepdata)
            break
        if not(Usernames == ""):
            Finder(Usernames, Keepdata2)
            break
        if not(Password == ""):
            Finder(Password, Keepdata3)
            break

def Finder(Value, Data):
    for Info in range(len(Data)):
        if Value == Data[Info]:
            return Keepdata

#Read function and corresponding code

def read(Shortcut):
    global Keepdata
    global Keepdata2
    global Keepdata3
    Keepdata = [x.strip() for x in open("Shortcuts.txt").readlines()]
    Keepdata2 = [x.strip() for x in open("Usernames.txt").readlines()]
    Keepdata3 = [x.strip() for x in open("Passwords.txt").readlines()]
    for Info in range(len(Keepdata)):
        if Shortcut[0] == Keepdata[Info]:
            Shortcutread = Keepdata[Info]
            Passwordread = Keepdata2[Info]
            Usernameread = Keepdata3[Info]
            return Shortcutread, Usernameread, Passwordread
