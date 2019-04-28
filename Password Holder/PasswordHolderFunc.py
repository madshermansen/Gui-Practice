#Add function and corresponding code
def add(): #Add Shortcut, Password, and Username to directory
    Shortcut = input("Shortcut: ")
    Username = input("Username: ")
    Password = input("Password: ")
    Shortcutwrite(Shortcut)
    Usernamewrite(Username)
    Passwordwrite(Password)

def Shortcutwrite(Shortcut): #Write Shortcut in Shorcut.txt
    typeShort = open("Shortcuts.txt", "w")
    Keepdata = [x.strip() for x in open("Shortcuts.txt").readlines()]
    for Info in Keepdata:
        typeShort.write(str(Info) + "\n")
    typeShort.write(Shortcut + "\n")
    typeShort.close()

def Usernamewrite(Username): #Write Username in Username.txt
    typeUser = open("Username.txt", "w")
    Keepdata = [x.strip() for x in open("Username.txt").readlines()]
    for Info in Keepdata:
        typeUser.write(str(Info) + "\n")
    typeUser.write(Username + "\n")
    typeUser.close()

def Passwordwrite(Password): #Write Password in Passwords.txt
    typePass = open("Passwords.txt", "w")
    Keepdata = [x.strip() for x in open("Passwords.txt").readlines()]
    for Info in Keepdata:
        typePass.write(str(Info) + "\n")
    typePass.write(Password + "\n")
    typePass.close()

#Remove function and corresponding code

#Find function and correspondding code

#Open function and corresponding code
