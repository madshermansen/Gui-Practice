from AsciiDic import *

Word = input("Enter the word: ")
for a in range(6):
    printAsciivar = ""
    for i in list(Word):
        printAsciivar = printAsciivar + AsciiArt["Graffitti"][i][a]
    print(printAsciivar)