from __future__ import unicode_literals
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
import youtube_dl
import tkinter as tk

Downloader = tk.Tk()

Downloader.title("Youtube Downloader+")
Downloader.geometry("370x60")
Downloader.resizable(False, False)
Downloader.configure(background="#222222")


def download(): #Download function
    try:
        if QualityPick.get() == "MP3":
            ydl_opts = {
                'format': 'bestaudio/mp3',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        elif QualityPick.get() == "M4A":
            ydl_opts = {
                'format': 'bestaudio/m4a',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'm4a',
                    'preferredquality': '192',
                }],
            }
        elif QualityPick.get() == "WAV":
            ydl_opts = {
                'format': 'bestaudio/wav',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                    'preferredquality': '192',
                }],
            }
        elif QualityPick.get() == "Best Video and Audio Quality":
            ydl_opts = {
                'format': '(bestvideo[width>=1920]/bestvideo)+bestaudio/best'
            }
        elif QualityPick.get() == "MP4 1080p":
            ydl_opts = {
                'format': '137',
            }
        elif QualityPick.get() == "MP4 720p":
            ydl_opts = {
                'format': "136"
            }
        elif QualityPick.get() == "MP4 480p":
            ydl_opts = {
                'format': "135"
            }
        elif QualityPick.get() == "MP4 360p":
            ydl_opts = {
                'format': "134"

            }
        else:
            ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([Youtubelink.get()])
    except:
        print("Program Error")


#Buttons and entry fields
DownloadButton = Button(Downloader, text="Download", command=download)
DownloadButton.grid(column=0, row=0, sticky=W)

Youtubelink = Entry(Downloader, width=33, foreground="#43464A")
Youtubelink.insert(0, "Enter Link...")
Youtubelink.grid(column=2, row=0, sticky=W)

#Labels and Quality selection
Quality = Label(Downloader, text="", background="#222222", foreground="#ffffff")
Quality.grid(column=0, row=1, sticky=W)

QualityPick = Combobox(Downloader, width="30", background="#222222")
QualityPick['values'] = ("Best Video and Audio Quality", "MP4 1080p", "MP4 720p", "MP4 480p", "MP4 360p", "M4A", "MP3", "WAV")
QualityPick.current(0)
QualityPick.grid(column=2, row=1, sticky=W)

#Pack
Filler = Label(Downloader, text="", background="#222222", width=9)
Filler.grid(column=1, row=0, sticky=W)
Filler2 = Label(Downloader, text="", background="#222222")
Filler2.grid(column=1, row=1, sticky=W)

Downloader.mainloop()
