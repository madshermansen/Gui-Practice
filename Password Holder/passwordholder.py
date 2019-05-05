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
        passwordholderfunc.add(values[1], values[2], values[3])
    elif event == "Remove":
        passwordholderfunc.remover(values[1], values[2], values[3], values[4])
    elif event == "Open/Read":
        try:
            Shortcutread, Usernameread, Passwordread = passwordholderfunc.read(values[4])
        except:
            Shortcutread, Usernameread, Passwordread = "", "", ""
    if event == "Find":
        try:
            if values[1] == "" and values[2] == "" and values[3] == "":
                namelist = passwordholderfunc.Setnamelist()
            else:
                namelist = passwordholderfunc.find(values[1], values[2], values[3])
        except:
            namelist = passwordholderfunc.Setnamelist()
    else:
        namelist = passwordholderfunc.Setnamelist()
    Positionx = Holder.CurrentLocation()
    Holder.Close()
