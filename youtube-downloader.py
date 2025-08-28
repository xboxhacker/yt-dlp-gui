import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import os

def browse_cookies():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    cookies_var.set(file_path)

def browse_save_location():
    folder_path = filedialog.askdirectory()
    save_var.set(folder_path)

def download_video():
    url = url_var.get()
    cookies = cookies_var.get()
    save_path = save_var.get()
    keep_raw = keep_raw_var.get()
    audio_only = audio_var.get()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return

    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s') if save_path else '%(title)s.%(ext)s',
    }

    if cookies:
        ydl_opts['cookiefile'] = cookies

    if audio_only:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        ydl_opts['format'] = 'bestvideo+bestaudio/best'

    if keep_raw:
        ydl_opts['keepvideo'] = True

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {str(e)}")

root = tk.Tk()
root.title("YouTube Downloader")

url_var = tk.StringVar()
cookies_var = tk.StringVar()
save_var = tk.StringVar()
keep_raw_var = tk.BooleanVar()
audio_var = tk.BooleanVar()

tk.Label(root, text="YouTube Video URL:").grid(row=0, column=0, sticky='w')
tk.Entry(root, textvariable=url_var, width=50).grid(row=0, column=1, columnspan=2)

tk.Label(root, text="Cookies File (optional):").grid(row=1, column=0, sticky='w')
tk.Entry(root, textvariable=cookies_var, width=38).grid(row=1, column=1)
tk.Button(root, text="Browse", command=browse_cookies).grid(row=1, column=2)

tk.Label(root, text="Save Location:").grid(row=2, column=0, sticky='w')
tk.Entry(root, textvariable=save_var, width=38).grid(row=2, column=1)
tk.Button(root, text="Browse", command=browse_save_location).grid(row=2, column=2)

tk.Checkbutton(root, text="Keep Raw Files (-k)", variable=keep_raw_var).grid(row=3, column=0, sticky='w')
tk.Checkbutton(root, text="Audio Only (MP3)", variable=audio_var).grid(row=3, column=1, sticky='w')

tk.Button(root, text="Download", command=download_video, width=20, bg='green', fg='white').grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
