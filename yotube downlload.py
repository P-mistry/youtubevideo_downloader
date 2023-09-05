import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = entry_url.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo("Download Complete", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and configure the URL entry field
entry_url = tk.Entry(root, width=40)
entry_url.pack(pady=10)

# Create the Download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

# Run the GUI
root.mainloop()
