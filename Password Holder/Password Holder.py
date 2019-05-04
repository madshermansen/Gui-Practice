import passwordholderfunc

Shortcutread = "Shortcut"
Usernameread = "Username"
Passwordread = "Password"
namelist = passwordholderfunc.Setnamelist()

while True:
    try:
        Holder = passwordholderfunc.SetHolder(Shortcutread,
                                              Usernameread,
                                              Passwordread,
                                              Positionx,
                                              namelist)
    except:
        Holder = passwordholderfunc.SetHolder(Shortcutread,
                                              Usernameread,
                                              Passwordread,
                                              None,
                                              namelist)
    event, values = Holder.Read()
    Shortcutread = ""
    Usernameread = ""
    Passwordread = ""
    if event == "Exit" or event == None:
        break
    elif event == "Add":
        passwordholderfunc.add(values[0], values[1], values[2])
    elif event == "Remove":
        passwordholderfunc.remover(values[0], values[1], values[2], values[3])
    elif event == "Open/Read":
        try:
            Shortcutread, Usernameread, Passwordread = passwordholderfunc.read(values[3])
        except:
            Shortcutread, Usernameread, Passwordread = "", "", ""
    if event == "Find":
        try:
            if values[0] == "" and values[1] == "" and values[2] == "":
                namelist = passwordholderfunc.Setnamelist()
            else:
                namelist = passwordholderfunc.find(values[0], values[1], values[2])
        except:
            namelist = passwordholderfunc.Setnamelist()
    else:
        namelist = passwordholderfunc.Setnamelist()
    Positionx = Holder.CurrentLocation()
    Holder.Close()
