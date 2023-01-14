import tkinter as tk
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        yt_link = link.get()
        yt = YouTube(yt_link)
        video = yt.streams.get_highest_resolution()
        video.download()
    except Exception as err:
        print("Youtube link is invalid")
    print("Download Complete")


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Link input
url_val = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_val)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
