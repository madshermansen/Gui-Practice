import praw
import re
import time
import PySimpleGUI as sg

def BotON():
    for comment in subreddit.stream.comments():
        time.sleep(0.3)
        print(comment.body)
        if re.search(RedditScan[1], comment.body, re.IGNORECASE):
            comment.reply(RedditScan[2])
            print(RedditScan[2])

def CheckAccount():
    reddit = praw.Reddit(client_id=values[2],
                         client_secret=values[3],
                         password=values[1],
                         user_agent=values[4],
                         username=values[0])
    try:
        return reddit.user.me()
    except:
        return False

import RedditBotGUI
Account = False
while Account == False:
    event, values = RedditBotGUI.RedditBot()
    Account = CheckAccount()
    RedditBotGUI.layout2 = [
        [sg.Text("Logged in as " + str(Account))],
        [sg.Text("Subreddit", size=(15, 1)), sg.InputText('')],
        [sg.Text("Bot Respond to", size=(15, 1)), sg.InputText('')],
        [sg.Text("Bot Reply", size=(15, 1)), sg.InputText('')],
        [sg.Submit("Turn On", size=(15, 1)), sg.Exit()]
    ]


    if event is None or event == 'Exit':
        break
    while Account != None and Account != False:
        event, RedditScan = RedditBotGUI.Start()
        if event is None or event == 'Exit':
            break
        try:
            if event == "Turn On":
                reddit = praw.Reddit(client_id=values[2],
                                     client_secret=values[3],
                                     password=values[1],
                                     user_agent=values[4],
                                     username=values[0])
                subreddit = reddit.subreddit(RedditScan[0])
                print = sg.Print
                BotON()

        except:
            RedditBotGUI.layout2 = [
                      [sg.Text("Logged in as " + str(Account) + "                      Please Enter Data")],
                      [sg.Text("Subreddit", size=(15, 1)), sg.InputText('')],
                      [sg.Text("Bot Respond to", size=(15, 1)), sg.InputText('')],
                      [sg.Text("Bot Reply", size=(15, 1)), sg.InputText('')],
                      [sg.Submit("Turn On", size=(15, 1)), sg.Exit()]
            ]
