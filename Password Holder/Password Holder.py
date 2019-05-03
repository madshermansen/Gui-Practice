import PasswordHolderFunc
import PySimpleGUI as sg

Shortcutread = "Shortcut"
Usernameread = "Username"
Passwordread = "Password"
namelist = PasswordHolderFunc.Setnamelist()

while True:
    try:
        Holder = PasswordHolderFunc.SetHolder(Shortcutread, Usernameread, Passwordread, Positionx, namelist)
    except:
        Holder = PasswordHolderFunc.SetHolder(Shortcutread, Usernameread, Passwordread, None, namelist)
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
    if event == "Find":
        try:
            if values[0] == "" and values[1] == "" and values[2] == "":
                namelist = PasswordHolderFunc.Setnamelist()
            else:
                namelist = PasswordHolderFunc.find(values[0], values[1], values[2])
        except:
            namelist = PasswordHolderFunc.Setnamelist()
    else:
        namelist = PasswordHolderFunc.Setnamelist()
    Positionx = Holder.CurrentLocation()
    Holder.Close()
