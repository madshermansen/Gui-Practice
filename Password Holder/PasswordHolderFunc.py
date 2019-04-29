#Add function and corresponding code

def add(): #Add Shortcut, Password, and Usernames to directory
    Shortcut = input("Shortcut: ")
    Usernames = input("Username: ")
    Password = input("Password: ")
    Shortcutwrite(Shortcut)
    Usernameswrite(Usernames)
    Passwordwrite(Password)

def Shortcutwrite(Shortcut): #Write Shortcut in Shorcut.txt
    try:
        Keepdata = [x.strip() for x in open("Shortcuts.txt").readlines()]
        typeShort = open("Shortcuts.txt", "w")
    except:
        typeShort = open("Shortcuts.txt", "w")
        Keepdata = [x.strip() for x in open("Shortcuts.txt").readlines()]
    for Info in Keepdata:
        typeShort.write(str(Info) + "\n")
    typeShort.write(Shortcut + "\n")
    typeShort.close()

def Usernameswrite(Usernames): #Write Usernames in Usernames.txt
    try:
        Keepdata = [x.strip() for x in open("Usernames.txt").readlines()]
        typeUser = open("Usernames.txt", "w")
    except:
        typeUser = open("Usernames.txt", "w")
        Keepdata = [x.strip() for x in open("Usernames.txt").readlines()]
    for Info in Keepdata:
        typeUser.write(str(Info) + "\n")
    typeUser.write(Usernames + "\n")
    typeUser.close()

def Passwordwrite(Password): #Write Password in Passwords.txt
    try:
        Keepdata = [x.strip() for x in open("Passwords.txt").readlines()]
        typePass = open("Passwords.txt", "w")
    except:
        typePass = open("Passwords.txt", "w")
        Keepdata = [x.strip() for x in open("Passwords.txt").readlines()]
    for Info in Keepdata:
        typePass.write(str(Info) + "\n")
    typePass.write(Password + "\n")
    typePass.close()

#Remove function and corresponding code

def remove(): #Remove data from directory
    input("")

#Find function and correspondding code

def find():
    global Keepdata
    global Keepdata2
    global Keepdata3
    Keepdata = [x.strip() for x in open("Shortcuts.txt").readlines()]
    Keepdata2 = [x.strip() for x in open("Usernames.txt").readlines()]
    Keepdata3 = [x.strip() for x in open("Passwords.txt").readlines()]
    while True:
        Shortcut = input("What is the shortcut?: ")
        if not(Shortcut == ""):
            print("")
            Findshortcut(Shortcut)
            break
        Usernames = input("What is the username?: ")
        if not(Usernames == ""):
            print("")
            FindUsernames(Usernames)
            break
        Password = input("What is the password?: ")
        if not(Password == ""):
            print("")
            Findpassword(Password)
            break
        print("")

def Findshortcut(Shortcut):
    print("Shortcut: Username:Password \n")
    for Info in range(len(Keepdata)):
        if Shortcut == Keepdata[Info]:
            print(Keepdata[Info] + ": " + Keepdata2[Info] + ":" + Keepdata3[Info])
           

def FindUsernames(Usernames):
    print("Shortcut: Username:Password \n")
    for Info in range(len(Keepdata)):
        if Usernames == Keepdata2[Info]:
            print(Keepdata[Info] + ": " + Keepdata2[Info] + ":" + Keepdata3[Info])

def Findpassword(Password):
    print("Shortcut: Username:Password \n")
    for Info in range(len(Keepdata)):
        if Password == Keepdata3[Info]:
            print(Keepdata[Info] + ": " + Keepdata2[Info] + ":" + Keepdata3[Info])

#Open function and corresponding code

def Open():
    input("")
