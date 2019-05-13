"""
Name: Password Manager
Made By: Mads Hermansen
Github: https://github.com/KarlofKuwait
Date: 05/05/2019
"""
from tkinter import filedialog
import os
import errno
import PySimpleGUI as sg
# Make sure the files are there
filename = ["Userdata/Shortcuts.txt", "Userdata/Usernames.txt", "Userdata/Passwords.txt"]
for Info in filename:
    if not os.path.exists(os.path.dirname(Info)):
        try:
            os.makedirs(os.path.dirname(Info))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    try:
        [x.strip() for x in open(Info).readlines()]
    except:
        with open(Info, "w") as f:
            f.write("")

# Add function and corresponding code
def add(Shortcut, Usernames, Password):
    if Shortcut == "" or Usernames == "" or Password == "":
        setentervaluepage("Please enter values")
        return
    Shortcutwrite(Shortcut)
    Usernameswrite(Usernames)
    Passwordwrite(Password)

def Shortcutwrite(Shortcut):
    try:
        Keepdata = [x.strip() for x in open("Userdata/Shortcuts.txt").readlines()]
        typeShort = open("Userdata/Shortcuts.txt", "w")
    except NameError:
        typeShort = open("Userdata/Shortcuts.txt", "w")
        Keepdata = [x.strip() for x in open("Userdata/Shortcuts.txt").readlines()]
    for Info in Keepdata:
        typeShort.write(str(Info) + "\n")
    typeShort.write(Shortcut + "\n")
    typeShort.close()

def Usernameswrite(Usernames):
    try:
        Keepdata = [x.strip() for x in open("Userdata/Usernames.txt").readlines()]
        typeUser = open("Userdata/Usernames.txt", "w")
    except NameError:
        typeUser = open("Userdata/Usernames.txt", "w")
        Keepdata = [x.strip() for x in open("Userdata/Usernames.txt").readlines()]
    for Info in Keepdata:
        typeUser.write(str(Info) + "\n")
    typeUser.write(Usernames + "\n")
    typeUser.close()

def Passwordwrite(Password):
    try:
        Keepdata = [x.strip() for x in open("Userdata/Passwords.txt").readlines()]
        typePass = open("Userdata/Passwords.txt", "w")
    except NameError:
        typePass = open("Userdata/Passwords.txt", "w")
        Keepdata = [x.strip() for x in open("Userdata/Passwords.txt").readlines()]
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
    Keepdata = [x.strip() for x in open("Userdata/Shortcuts.txt").readlines()]
    Keepdata2 = [x.strip() for x in open("Userdata/Usernames.txt").readlines()]
    Keepdata3 = [x.strip() for x in open("Userdata/Passwords.txt").readlines()]
    if Testfor != []:
        Testfor = Testfor[0].split(": ")
        Shortcut = Testfor[0]
        Username = Testfor[1]
        Password = Testfor[2]
        Removerselect(Shortcut, Username, Password)
        return
    elif Shortcut == "" and Usernames == "" and Password == "":
        setentervaluepage("Please enter values")
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
    for I in range(len(Keepdata)):
        if Shortcut == Keepdata[I] and Username == Keepdata2[I] and Password == Keepdata3[I]:
            RemoveIndex.append(I)
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
        Keepdata.pop(Info)
        Keepdata2.pop(Info)
        Keepdata3.pop(Info)
    typeShort = open("Userdata/Shortcuts.txt", "w")
    for Info in Keepdata:
        typeShort.write(str(Info) + "\n")
    typeShort.close()
    typeUser = open("Userdata/Usernames.txt", "w")
    for Info in Keepdata2:
        typeUser.write(str(Info) + "\n")
    typeUser.close()
    typePass = open("Userdata/Passwords.txt", "w")
    for Info in Keepdata3:
        typePass.write(str(Info) + "\n")
    typePass.close()
    setentervaluepage("Removed " + str(len(RemoveIndex)) + " line(s)")

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
    Keepdata = [x.strip() for x in open("Userdata/Shortcuts.txt").readlines()]
    Keepdata2 = [x.strip() for x in open("Userdata/Usernames.txt").readlines()]
    Keepdata3 = [x.strip() for x in open("Userdata/Passwords.txt").readlines()]
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
        names = [x.strip() for x in open("Userdata/Shortcuts.txt").readlines()]
        names2 = [x.strip() for x in open("Userdata/Usernames.txt").readlines()]
        names3 = [x.strip() for x in open("Userdata/Passwords.txt").readlines()]
        namelist = []
        for Info in range(len(names)):
            namelist.append(names[Info] + ": " + names2[Info] + ": " + names3[Info])
    except:
        namelist = []
    return namelist


def SetHolder(Shortcutread, Usernameread, Passwordread, Positionx, namelist):
    Holderlayout = [
        [sg.ButtonMenu("Menu",
                       ["&Menu", ["&About", "&Save as", "E&xit"]],
                       button_color=("white", "#111111")),
         sg.Stretch(),
         sg.ButtonMenu("List",
                       ["&List", ["&Reload"]],
                       button_color=("white", "#111111")),
         sg.Stretch()
         ],
        [sg.InputText(Shortcutread,
                      size=(37, 1),
                      background_color="#292929",
                      text_color="white")],
        [sg.InputText(Usernameread,
                      size=(37, 1),
                      background_color="#292929",
                      text_color="white")],
        [sg.InputText(Passwordread,
                      size=(37, 1),
                      background_color="#292929",
                      text_color="white")],
        [sg.Listbox(values=namelist,
                    size=(35, 10),
                    background_color="#292929",
                    text_color="white")],
        [sg.Submit("Add", size=(15, 1),
                   button_color=("white", "#191919")),
         sg.Submit("Remove", size=(15, 1),
                   button_color=("white", "#191919"))],
        [sg.Submit("Find", size=(15, 1),
                   button_color=("white", "#191919")),
         sg.Submit("Open/Read", size=(15, 1),
                   button_color=("white", "#191919"))]
    ]
    global Holder
    try:
        Holder = sg.Window("Password Holder",
                           background_color="#191919",
                           button_color=None,
                           no_titlebar=False,
                           grab_anywhere=False,
                           icon="Image/Logo.ico",
                           location=(Positionx[0],
                                     Positionx[1])).Layout(Holderlayout)
    except:
        Holder = sg.Window("Password Holder",
                           background_color="#191919",
                           button_color=None,
                           no_titlebar=False,
                           icon="Image/Logo.ico",
                           grab_anywhere=False,).Layout(Holderlayout)
    return Holder

def SetAbout():
    aboutlayout = [
        [sg.Text("Name: Password Manager",
                 background_color="white")],
        [sg.Text("Made By: Mads Hermansen",
                 background_color="white")],
        [sg.Text("Github: https://github.com/KarlofKuwait",
                 background_color="white",)]
    ]
    about = sg.Window("About",
                      background_color="white",
                      button_color=None,
                      no_titlebar=False,
                      icon="Image/Logo.ico",
                      grab_anywhere=True).Layout(aboutlayout)
    return about

def setentervaluepage(Message):
    Messagelayout = [
        [sg.Text(Message,
                 background_color="white")]
    ]
    messages = sg.Window("Message",
                      background_color="white",
                      button_color=None,
                      no_titlebar=False,
                      icon = "Image/Logo.ico",
                      grab_anywhere=True).Layout(Messagelayout)
    messages.Read()

def Saveas(NAMELIST):
    try:
        filename = filedialog.asksaveasfilename()
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        typeSave = open(filename, "w")
        for Info in NAMELIST:
            typeSave.write(str(Info) + "\n")
        typeSave.close()
    except:
        pass

import PySimpleGUI as sg

def Genpass(GENLIST, LENGTH):
    import os
    PASSWORD = ""
    if GENLIST == []:
        return PASSWORD
    try:
        for i in range(int(LENGTH)):
            random = list(os.urandom(1))
            while not(random[0] <= len(GENLIST)):
                random = list(os.urandom(1))
            PASSWORD += GENLIST[random[0]-1]
        return PASSWORD
    except:
        pass

def Makegenlist(lowercase=False,
                uppercase=False,
                digits=False,
                symbols=False):
    import string
    GENLIST = []
    if lowercase == True:
        GENLIST += list(string.ascii_lowercase)
    if uppercase == True:
        GENLIST += list(string.ascii_uppercase)
    if digits == True:
        GENLIST += list(string.digits)
    if symbols == True:
        GENLIST += list(string.punctuation)
    return GENLIST

def MakePassGenGUI():
    LengthBox = [x for x in range(1, 257)]
    passgenlayout = [
        [sg.Text("Password Length: ",
                 size=(23, 1),
                 background_color="#191919",
                 text_color="white"),
         sg.InputCombo(LengthBox,
                 background_color="#191919",
                 text_color="white",
                 key="Length",
                 size=(12, 1),)],
        [sg.Text("Include Symbols: ",
                 size=(23, 1),
                 background_color="#191919",
                 text_color="white"),
         sg.Checkbox("( e.g. @#$% )",
                     default=True,
                     key="Symbols",
                     background_color="#191919",
                     text_color="white")],
        [sg.Text("Include Numbers: ",
                 size=(23, 1),
                 background_color="#191919",
                 text_color="white"),
         sg.Checkbox("( e.g. 123456 )",
                     default=True,
                     key="Digits",
                     background_color="#191919",
                     text_color="white")],
        [sg.Text("Include Lowercase characters: ",
                 size=(23, 1),
                 background_color="#191919",
                 text_color="white"),
         sg.Checkbox("( e.g. abcdefgh )",
                     default=True,
                     key="Lowercase",
                     background_color="#191919",
                     text_color="white")],
        [sg.Text("Include Uppercase characters: ",
                 size=(23, 1),
                 background_color="#191919",
                 text_color="white"),
         sg.Checkbox("( e.g. ABCDEFGH )",
                     default=True,
                     key="Uppercase",
                     background_color="#191919",
                     text_color="white")],
        [sg.Text("Exclude similar characters: ",
                 size=(23, 1),
                 background_color="#191919",
                 text_color="white"),
         sg.Checkbox("( e.g. i, l, 1, L, o, 0, O )",
                     default=False,
                     key="Similar",
                     background_color="#191919",
                     text_color="white")],
        [sg.Text("Save preference:",
                 size=(23, 1),
                 background_color="#191919",
                 text_color="white"),
         sg.Checkbox("(saves settings for later use)",
                     default=False,
                     key="Settings",
                     background_color="#191919",
                     text_color="white")],
        [sg.InputText("", key="_text_",
                      text_color="LightGreen",
                      background_color="#292929")],
        [sg.Exit("Exit",
                   button_color=("white", "#191919")),
         sg.Submit("Generate",
                   button_color=("white", "#191919"))]
    ]
    Passgen = sg.Window("Password Generator",
                           background_color="#191919",
                           button_color=None,
                           no_titlebar=False,
                           icon="Image/Logo.ico",
                           grab_anywhere=False,).Layout(passgenlayout)
    while True:
        event2, values2 = Passgen.Read()
        if event2 == None or event2 == "Exit":
            break
        Length = values2["Length"]
        symbols = values2["Symbols"]
        digits = values2["Digits"]
        uppercase = values2["Uppercase"]
        lowercase = values2["Lowercase"]
        Password = Genpass((Makegenlist(lowercase, uppercase, digits, symbols)), Length)
        Passgen.FindElement("_text_").Update(Password)
