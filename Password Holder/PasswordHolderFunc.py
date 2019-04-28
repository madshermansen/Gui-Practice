def add(): #Add Shortcut, Password, and Username to directory
    global Shortcut
    global Password
    global Username
    Shortcut = input("Shortcut: ")
    Username = input("Username: ")
    Password = input("Password: ")
    Shortcutwrite()
    Passwordwrite()
    Usernamewrite()

def Shortcutwrite(): # Write Shortcut in Shorcut.txt
    typeShort = open("Shortcuts.txt", "w")
    Keepdata = [x.strip() for x in open("Shortcuts.txt").readlines()]
    for Info in Keepdata:
        typeShort.write(str(Info) + "\n")
    typeShort.write(Shortcut + "\n")
    typeShort.close()

def Passwordwrite(): # Write Password in Passwords.txt
    typePass = open("Passwords.txt", "w")
    Keepdata = [x.strip() for x in open("Passwords.txt").readlines()]
    for Info in Keepdata:
        typePass.write(str(Info) + "\n")
    typePass.write(Password + "\n")
    typePass.close()

def Usernamewrite(): #Write Username in Username.txt
    typeUser = open("Username.txt", "w")
    Keepdata = [x.strip() for x in open("Username.txt").readlines()]
    for Info in Keepdata:
        typeUser.write(str(Info) + "\n")
    typeUser.write(Username + "\n")
    typeUser.close()