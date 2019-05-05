"""
Name: Password Manager
Made By: Mads Hermansen
Github: https://github.com/KarlofKuwait
Date: 05/05/2019
"""
import passwordholderfunc as phf

SHORTCUT_READ = "Shortcut"
USERNAME_READ = "Username"
PASSWORD_READ = "Password"

NAMELIST = phf.Setnamelist()

while True:
    try:
        HOLDER = phf.SetHolder(SHORTCUT_READ, USERNAME_READ, PASSWORD_READ, POSITION, NAMELIST)
    except NameError:
        HOLDER = phf.SetHolder(SHORTCUT_READ, USERNAME_READ, PASSWORD_READ, None, NAMELIST)
    EVENT, VALUES = HOLDER.Read()
    SHORTCUT_READ = ""
    USERNAME_READ = ""
    PASSWORD_READ = ""
    VALUES.remove(None)
    if EVENT == "Exit" or EVENT == None or "Exit" in VALUES:
        break
    elif "About" in VALUES:
        About = phf.SetAbout()
        About.Read()
    elif "Save as" in VALUES:
        phf.Saveas(NAMELIST)
    elif EVENT == "Add":
        phf.add(VALUES[3], VALUES[4], VALUES[5])
    elif EVENT == "Remove":
        phf.remover(VALUES[3], VALUES[4], VALUES[5], VALUES[6])
    elif EVENT == "Open/Read":
        try:
            SHORTCUT_READ, USERNAME_READ, PASSWORD_READ = phf.read(VALUES[6])
        except:
            SHORTCUT_READ, USERNAME_READ, PASSWORD_READ = "", "", ""
    if EVENT == "Find":
        try:
            if VALUES[3] == "" and VALUES[4] == "" and VALUES[5] == "":
                NAMELIST = phf.Setnamelist()
            else:
                NAMELIST = phf.find(VALUES[3], VALUES[4], VALUES[5])
        except NameError:
            NAMELIST = phf.Setnamelist()
    else:
        NAMELIST = phf.Setnamelist()
    POSITION = HOLDER.CurrentLocation()
    HOLDER.Close()
