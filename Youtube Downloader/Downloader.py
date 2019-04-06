from __future__ import unicode_literals
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import youtube_dl
import tkinter as tk

Downloader = tk.Tk()

Downloader.title("Youtube Downloader+")
Downloader.geometry("325x110")
Downloader.resizable(False, False)
Downloader.configure(background="#222222")

def grablocation(): #Get file location
    while Location.get() != "":
        Location.delete(0, "end")
    if Location.get() == "":
        return Location.insert(0, filedialog.askdirectory())

def download(): #Download function
    try:
        if QualityPick.get() == "MP3":
            ydl_opts = {
                'format': 'bestaudio/mp3',
                'outtmpl': Location.get() + '/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        elif QualityPick.get() == "M4A":
            ydl_opts = {
                'format': 'bestaudio/m4a',
                'outtmpl': Location.get() + '/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'm4a',
                    'preferredquality': '192',
                }],
            }
        elif QualityPick.get() == "WAV":
            ydl_opts = {
                'format': 'bestaudio/wav',
                'outtmpl': Location.get() + '/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                    'preferredquality': '192',
                }],
            }
        elif QualityPick.get() == "Best Video and Audio Quality":
            ydl_opts = {
                'outtmpl': Location.get() + '/%(title)s.%(ext)s',
                'format': '(bestvideo[width>=1920]/bestvideo)+bestaudio/best'

            }
        elif QualityPick.get() == "MP4 1080p":
            ydl_opts = {
                'outtmpl': Location.get() + '/%(title)s.%(ext)s',
                'format': '137',
            }
        elif QualityPick.get() == "MP4 720p":
            ydl_opts = {
                'outtmpl': Location.get() + '/%(title)s.%(ext)s',
                'format': "136"
            }
        elif QualityPick.get() == "MP4 480p":
            ydl_opts = {
                'outtmpl': Location.get() + '/%(title)s.%(ext)s',
                'format': "135"
            }
        elif QualityPick.get() == "MP4 360p":
            ydl_opts = {
                'outtmpl': Location.get() + '/%(title)s.%(ext)s',
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
DownloadButton.grid(column=1, row=1, sticky=W)

Youtubelink = Entry(Downloader, width=33, foreground="#43464A")
Youtubelink.insert(0, "Enter Link...")
Youtubelink.grid(column=3, row=1, sticky=W)

#Labels and Quality selection
Quality = Label(Downloader, text="", background="#222222", foreground="#ffffff")
Quality.grid(column=0, row=2, sticky=W)

QualityPick = Combobox(Downloader, width="30", background="#222222")
QualityPick['values'] = ("Best Video and Audio Quality", "MP4 1080p", "MP4 720p", "MP4 480p", "MP4 360p", "M4A", "MP3", "WAV")
QualityPick.current(0)
QualityPick.grid(column=3, row=2, sticky=W)

#Pack
Filler = Label(Downloader, text="", background="#222222", width=2)
Filler.grid(column=0, row=0, sticky=W)
Filler = Label(Downloader, text="", background="#222222", width=2)
Filler.grid(column=0, row=1, sticky=W)
Filler2 = Label(Downloader, text="", background="#222222", width=1)
Filler2.grid(column=2, row=1, sticky=W)

Location = Entry(Downloader, width=33)
Location.grid(column=3, row=3)
FindLocation = Button(Downloader, text="Location", command=grablocation)
FindLocation.grid(column=1, row=3, sticky=W)

Downloader.mainloop()
