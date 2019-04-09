from __future__ import unicode_literals
import youtube_dl
import PySimpleGUI as sg

def download(): #Download function
    try:
        if values[1] == "MP3":
            ydl_opts = {
                'format': 'bestaudio/mp3',
                'outtmpl': values[2] + '/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        elif values[1] == "M4A":
            ydl_opts = {
                'format': 'bestaudio/m4a',
                'outtmpl': values[2] + '/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'm4a',
                    'preferredquality': '192',
                }],
            }
        elif values[1] == "WAV":
            ydl_opts = {
                'format': 'bestaudio/wav',
                'outtmpl': values[2] + '/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                    'preferredquality': '192',
                }],
            }
        elif values[1] == "Best Video and Audio Quality":
            ydl_opts = {
                'outtmpl': values[2] + '/%(title)s.%(ext)s',
                'format': '(bestvideo[width>=1920]/bestvideo)+bestaudio/best'

            }
        elif values[1] == "MP4 1080p":
            ydl_opts = {
                'outtmpl': values[2] + '/%(title)s.%(ext)s',
                'format': '137',
            }
        elif values[1] == "MP4 720p":
            ydl_opts = {
                'outtmpl': values[2] + '/%(title)s.%(ext)s',
                'format': "136"
            }
        elif values[1] == "MP4 480p":
            ydl_opts = {
                'outtmpl': values[2] + '/%(title)s.%(ext)s',
                'format': "135"
            }
        elif values[1] == "MP4 360p":
            ydl_opts = {
                'outtmpl': values[2] + '/%(title)s.%(ext)s',
                'format': "134"
            }
        else:
            ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            for i in range(3000):
                progress_bar.UpdateBar(i + 1)
            ydl.download([values[0]])
            for i in range(7000):
                progress_bar.UpdateBar(i + i + 3000)
    except:
        print("Program Error")



layout = [
          [sg.Text('Link', size=(15, 1)), sg.InputText('')],
          [sg.Text('Quality', size=(15, 1)), sg.InputCombo(["Best Video and Audio Quality",
                                                            "MP4 1080p",
                                                            "MP4 720p",
                                                            "MP4 480p",
                                                            "MP4 360p",
                                                            "MP3",
                                                            "WAV",
                                                            "M4A"
                                                            ], size=(25, 100))],
          [sg.FolderBrowse('Location', size=(15, 1)), sg.InputText('')],
          [sg.ProgressBar(10000, orientation='h', key='progressbar')],
          [sg.Ok('Download'), sg.Exit()]


         ]

window = sg.Window('Youtube Downloader').Layout(layout)
progress_bar = window.FindElement('progressbar')

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if event == 'Download':
        download()
