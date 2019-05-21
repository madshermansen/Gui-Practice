"""
Name: Password Manager
Made By: Mads Hermansen
Github: https://github.com/KarlofKuwait
Date: 05/05/2019
"""

import passwordholderfunc as phf
def set_default():
    global HOLDER
    HOLDER.FindElement("Shortcutkey").Update(SHORTCUT_READ)
    HOLDER.FindElement("Usernamekey").Update(USERNAME_READ)
    HOLDER.FindElement("Passwordkey").Update(PASSWORD_READ)
    HOLDER.FindElement("Listboxkey").Update(NAMELIST)

if __name__ == "__main__":
    SHORTCUT_READ = "Shortcut"
    USERNAME_READ = "Username"
    PASSWORD_READ = "Password"
    NAMELIST = phf.Setnamelist()
    HOLDER = phf.SetHolder(SHORTCUT_READ, USERNAME_READ, PASSWORD_READ, None, NAMELIST)
    while True:
        EVENT, VALUES = HOLDER.Read()
        SHORTCUT_READ = ""
        USERNAME_READ = ""
        PASSWORD_READ = ""
        if EVENT == "Exit" or EVENT == None or VALUES[0] == "Exit":
            break
        elif EVENT == "Add":
            phf.add(VALUES["Shortcutkey"], VALUES["Usernamekey"], VALUES["Passwordkey"])
            NAMELIST = phf.Setnamelist()
            set_default()
        elif EVENT == "Remove":
            phf.remover(VALUES["Shortcutkey"], VALUES["Usernamekey"], VALUES["Passwordkey"], VALUES["Listboxkey"])
            NAMELIST = phf.Setnamelist()
            set_default()
        elif VALUES[0] == "About":
            About = phf.SetAbout()
            About.Read()
        elif VALUES[2] == "Reset":
            phf.reset()
            NAMELIST = phf.Setnamelist()
            set_default()
        elif EVENT == "Open/Read":
            try:
                SHORTCUT_READ, USERNAME_READ, PASSWORD_READ = phf.read(VALUES["Listboxkey"])
            except:
                SHORTCUT_READ, USERNAME_READ, PASSWORD_READ = "", "", ""
            set_default()
        elif VALUES[0] == "Password Generator":
            phf.MakePassGenGUI()
        elif VALUES[0] == "Save as":
            phf.Saveas(NAMELIST)
        elif EVENT == "Find":
            try:
                if VALUES["Shortcutkey"] == "" and VALUES["Usernamekey"] == "" and VALUES["Passwordkey"] == "":
                    NAMELIST = phf.Setnamelist()
                else:
                    NAMELIST = phf.find(VALUES["Shortcutkey"], VALUES["Usernamekey"], VALUES["Passwordkey"])
            except NameError:
                NAMELIST = phf.Setnamelist()
            set_default()
