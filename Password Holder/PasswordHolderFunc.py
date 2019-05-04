# Add function and corresponding code
import PySimpleGUI as sg

def add(Shortcut, Usernames, Password):
    if Shortcut == "" or Usernames == "" or Password == "":
        print("Please enter values")
        return
    Shortcutwrite(Shortcut)
    Usernameswrite(Usernames)
    Passwordwrite(Password)

def Shortcutwrite(Shortcut):
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

def Usernameswrite(Usernames):
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

def Passwordwrite(Password):
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

# Remove function and corresponding code

def remover(Shortcut, Usernames, Password, Testfor):
    global Keepdata
    global Keepdata2
    global Keepdata3
    global RemoveIndex
    RemoveIndex = []
    Keepdata = [x.strip() for x in open("Shortcuts.txt").readlines()]
    Keepdata2 = [x.strip() for x in open("Usernames.txt").readlines()]
    Keepdata3 = [x.strip() for x in open("Passwords.txt").readlines()]
    if Testfor != []:
        Testfor = Testfor[0].split(": ")
        Shortcut = Testfor[0]
        Username = Testfor[1]
        Password = Testfor[2]
        Removerselect(Shortcut, Username, Password)
        return
    elif Shortcut == "" and Usernames == "" and Password == "":
        print("Please enter values")
        return
    else:
        if Shortcut != "":
            RemoverText(Shortcut, Keepdata)
            return
        if Usernames != "":
            RemoverText(Usernames, Keepdata2)
            return
        if Password == "":
            RemoverText(Password, Keepdata3)
            return

def Removerselect(Shortcut, Username, Password):
    for Info in range(len(Keepdata)):
        if Shortcut == Keepdata[Info] and Username == Keepdata2[Info] and Password == Keepdata3[Info]:
            RemoveIndex.append(Info)
    RemoveIndex.reverse()
    Remover(RemoveIndex)

def RemoverText(Value, Data):
    for Info in range(len(Data)):
        if Value == Data[Info]:
            RemoveIndex.append(Info)
    RemoveIndex.reverse()
    Remover(RemoveIndex)

def Remover(RemoveIndex):
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

# Find function and correspondding code

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
    if Randomlist == []:
        Randomlist = FinderZero(Randomlist)
    return Randomlist

def FinderZero(Randomlist):
    if Randomlist == []:
        for Info in range(len(Keepdata)):
            namelistcheck = []
            namelistcheck.append(Keepdata[Info])
            if namelistcheck[0] == namelist[0]:
                Randomlist.append(Keepdata[Info] + ": " + Keepdata2[Info] + ": " + Keepdata3[Info])
    if Randomlist == []:
        for Info in range(len(Keepdata2)):
            namelistcheck = []
            namelistcheck.append(Keepdata2[Info])
            if namelistcheck[0] == namelist[1]:
                Randomlist.append(Keepdata[Info] + ": " + Keepdata2[Info] + ": " + Keepdata3[Info])
    if Randomlist == []:
        for Info in range(len(Keepdata3)):
            namelistcheck = []
            namelistcheck.append(Keepdata3[Info])
            if namelistcheck[0] == namelist[2]:
                Randomlist.append(Keepdata[Info] + ": " + Keepdata2[Info] + ": " + Keepdata3[Info])
    return Randomlist


# Read function and corresponding code

def read(Shortcut):
    Shortcut = Shortcut[0].split(": ")
    return Shortcut[0], Shortcut[1], Shortcut[2]

# Set namelist


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
        [sg.Text("Password Holder", background_color=("#555555"), font=("Helvetica")), sg.Exit("Reset", button_color=("black", "green")), sg.Exit(button_color=("black", "red"))],
        [sg.InputText(Shortcutread,
                      size=(37, 1))],
        [sg.InputText(Usernameread,
                      size=(37, 1))],
        [sg.InputText(Passwordread,
                      size=(37, 1))],
        [sg.Listbox(values=namelist,
                    size=(35, 10))],
        [sg.Submit("Add", size=(15, 1), button_color=("black", "turquoise")),
         sg.Submit("Remove", size=(15, 1), button_color=("black", "turquoise"))],
        [sg.Submit("Find", size=(15, 1), button_color=("black", "turquoise")),
         sg.Submit("Open/Read", size=(15, 1), button_color=("black", "turquoise"))]
    ]
    global Holder
    try:
        Holder = sg.Window("Password Holder",
                           background_color="#555555",
                           button_color=None,
                           no_titlebar=True,
                           grab_anywhere=True,
                           location=(Positionx[0],
                                     Positionx[1])).Layout(layout)
    except:
        Holder = sg.Window("Password Holder",
                           background_color="#555555",
                           button_color=None,
                           no_titlebar=True,
                           grab_anywhere=True,).Layout(layout)
    return Holder
