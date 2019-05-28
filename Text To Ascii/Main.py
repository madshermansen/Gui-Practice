from AsciiDic import *
import PySimpleGUI as sg


layout = [
    [sg.InputText("", key=("Input"))],
    [sg.Multiline("", size=(40, 20), key=("Output"))]
]

TranslatorWindow = sg.Window("Text To AsciiArt").Layout(layout)
while True:
    Event, Values = TranslatorWindow.ReadNonBlocking()
    Word = Values["Input"]
    for a in range(6):
        printAsciivar = ""
        for i in list(Word):
            printAsciivar = printAsciivar + AsciiArt["Graffitti"][i][a]
    TranslatorWindow.FindElement("Output").Update(printAsciivar)

