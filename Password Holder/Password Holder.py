import PasswordHolderFunc
import PySimpleGUI as sg

Shortcutread = "Shortcut"
Usernameread = "Username"
Passwordread = "Password"
try:
    names = [x.strip() for x in open("Shortcuts.txt").readlines()]
except:
    names = []

while True:
    layout = [
        [sg.InputText(Shortcutread, size=(37, 1))],
        [sg.InputText(Usernameread, size=(37, 1))],
        [sg.InputText(Passwordread, size=(37, 1))],
        [sg.Listbox(values=names, size=(35, 10))],
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
            names = PasswordHolderFunc.find(values[0], values[1], values[2])
        except:
            try:
                names = [x.strip() for x in open("Shortcuts.txt").readlines()]
            except:
                names = []
    print(names)




#Function = input("What function do you want to use?: ")

#if Function == "Find" or Function == "find":
 #   PasswordHolderFunc.find()
#elif Function == "Read" or Function == "read":
 #   PasswordHolderFunc.read()

