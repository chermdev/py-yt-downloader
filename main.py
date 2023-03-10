import tkinter as tk
import customtkinter
from pytube import YouTube


def on_progress(stream, chunk, bytes_remaining):
    # Get progress percentage
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))

    # Update progress percentage
    progress_p.configure(text=per + '%')
    progress_p.update()

    # Update progress bar
    progress_bar.set(float(percentage_of_completion) / 100)


def startDownload():
    try:
        yt_link = link.get()
        yt = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt.streams.get_highest_resolution()
        title.configure(text=yt.title, text_color="white")
        video.download()
        finish_label.configure(text="Downloaded!", text_color="white")
    except Exception as err:
        finish_label.configure(
            text="Youtube link is invalid", text_color="red")
        raise


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

# Finished Downloading
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

# Progress Percentage
progress_p = customtkinter.CTkLabel(app, text="0%")
progress_p.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
