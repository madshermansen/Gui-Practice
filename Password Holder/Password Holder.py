import PasswordHolderFunc
import PySimpleGUI as sg

Shortcutread = "Shortcut"
Usernameread = "Username"
Passwordread = "Password"
try:
    names = [x.strip() for x in open("Shortcuts.txt").readlines()]
    names2 = [x.strip() for x in open("Usernames.txt").readlines()]
    names3 = [x.strip() for x in open("Passwords.txt").readlines()]
    namelist = []
    for Info in range(len(names)):
        namelist.append(names[Info] + ": " + names2[Info] + ": " + names3[Info])
except:
    names = []



while True:
    layout = [
        [sg.InputText(Shortcutread, size=(37, 1))],
        [sg.InputText(Usernameread, size=(37, 1))],
        [sg.InputText(Passwordread, size=(37, 1))],
        [sg.Listbox(values=namelist, size=(35, 10))],
        [sg.Submit("Add", size=(15, 1)), sg.Submit("Remove", size=(15, 1))],
        [sg.Submit("Find", size=(15, 1)), sg.Submit("Open/Read", size=(15, 1))]
    ]
    Holder = sg.Window("Password Holder", icon='Logo/Logo.ico').Layout(layout)
    event, values = Holder.Read()
    Shortcutread = ""
    Usernameread = ""
    Passwordread = ""
    if event == "Close" or event == None:
        break
    elif event == "Add":
        PasswordHolderFunc.add(values[0], values[1], values[2])
    elif event == "Remove":
        PasswordHolderFunc.remover(values[0], values[1], values[2], values[3])
    elif event == "Open/Read":
        try:
            Shortcutread, Usernameread, Passwordread = PasswordHolderFunc.read(values[3])
        except:
            Shortcutread, Usernameread, Passwordread = "", "", ""
    try:
        names = [x.strip() for x in open("Shortcuts.txt").readlines()]
    except:
        names = []
    if event == "Find":
        try:

            if values[0] == "" and values[1] == "" and values[2] == "":
                try:
                    names = [x.strip() for x in open("Shortcuts.txt").readlines()]
                    names2 = [x.strip() for x in open("Usernames.txt").readlines()]
                    names3 = [x.strip() for x in open("Passwords.txt").readlines()]
                    namelist = []
                    for Info in range(len(names)):
                        namelist.append(names[Info] + ": " + names2[Info] + ": " + names3[Info])
                except:
                    namelist = []
            else:
                namelist = PasswordHolderFunc.find(values[0], values[1], values[2])
        except:
            try:
                names = [x.strip() for x in open("Shortcuts.txt").readlines()]
                names2 = [x.strip() for x in open("Usernames.txt").readlines()]
                names3 = [x.strip() for x in open("Passwords.txt").readlines()]
                namelist = []
                for Info in range(len(names)):
                    namelist.append(names[Info] + ": " + names2[Info] + ": " + names3[Info])
            except:
                namelist = []
    else:
        try:
            names = [x.strip() for x in open("Shortcuts.txt").readlines()]
            names2 = [x.strip() for x in open("Usernames.txt").readlines()]
            names3 = [x.strip() for x in open("Passwords.txt").readlines()]
            namelist = []
            for Info in range(len(names)):
                namelist.append(names[Info] + ": " + names2[Info] + ": " + names3[Info])
        except:
            namelist = []
    Holder.Close()
