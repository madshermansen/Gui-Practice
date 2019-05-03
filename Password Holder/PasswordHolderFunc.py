#Add function and corresponding code
import PySimpleGUI as sg

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
    global namelist
    namelist = []
    namelist.append(Shortcut)
    namelist.append(Username)
    namelist.append(Password)
    return Finder()



def Finder():
    global Keepdata
    global Keepdata2
    global Keepdata3
    Keepdata = [x.strip() for x in open("Shortcuts.txt").readlines()]
    Keepdata2 = [x.strip() for x in open("Usernames.txt").readlines()]
    Keepdata3 = [x.strip() for x in open("Passwords.txt").readlines()]

    Randomlist = []
    for Info in range(len(Keepdata)):
        namelistcheck = []
        namelistcheck.append(Keepdata[Info] + ": " + Keepdata2[Info] + ": " + Keepdata3[Info])
        for Info2 in range(len(namelistcheck)):
            namelistcheck = namelistcheck[0].split(": ")
        if namelistcheck == namelist:
            Randomlist.append(namelist[0] + ": " + namelist[1] + ": " + namelist[2])
    return Randomlist


#Read function and corresponding code

def read(Shortcut):
    Shortcut = Shortcut[0].split(": ")
    return Shortcut[0], Shortcut[1], Shortcut[2]

#Set namelist
def Setnamelist():
    global namelist
    try:
        names = [x.strip() for x in open("Shortcuts.txt").readlines()]
        names2 = [x.strip() for x in open("Usernames.txt").readlines()]
        names3 = [x.strip() for x in open("Passwords.txt").readlines()]
        namelist = []
        for Info in range(len(names)):
            namelist.append(names[Info] + ": " + names2[Info] + ": " + names3[Info])
    except:
        namelist = []
    return namelist

def SetHolder(Shortcutread, Usernameread, Passwordread, Positionx, namelist):
    layout = [
        [sg.InputText(Shortcutread, size=(37, 1))],
        [sg.InputText(Usernameread, size=(37, 1))],
        [sg.InputText(Passwordread, size=(37, 1))],
        [sg.Listbox(values=namelist, size=(35, 10))],
        [sg.Submit("Add", size=(15, 1)), sg.Submit("Remove", size=(15, 1))],
        [sg.Submit("Find", size=(15, 1)), sg.Submit("Open/Read", size=(15, 1))]
    ]
    global Holder
    try:
        Holder = sg.Window("Password Holder", icon='Logo/Logo.ico', background_color="#555555", button_color=None,
                           no_titlebar=False, location=(Positionx[0], Positionx[1])).Layout(layout)
    except:
        Holder = sg.Window("Password Holder", icon='Logo/Logo.ico', background_color="#555555", button_color=None,
                           no_titlebar=False).Layout(layout)
    return Holder
