# 🎵 YouTube Downloader (Video / Audio Only + Members-Only Support)

A **simple Python GUI YouTube downloader** built with [yt-dlp](https://github.com/yt-dlp/yt-dlp) and `tkinter`.  
Supports **normal videos**, **members-only content** (via cookies), **audio-only MP3 downloads**, and **optional raw file keeping**.

---

## ✨ Features

- 📥 **Download YouTube videos** in the best available quality.
- 🔓 **Download members-only videos** using your own `cookies.txt`.
- 🎧 **Audio Only (MP3)** mode with FFmpeg conversion.
- 🗂 **Keep Raw Files** option (`-k` equivalent).
- 📂 Choose custom **save location**.
- 🖱 Simple, clean **GUI** — no command-line needed.


## 📦 Requirements

- **Python 3.7+**
- **yt-dlp** – `pip install yt-dlp`
- **tkinter** – comes pre-installed with most Python distributions
- **FFmpeg** (optional but recommended for MP3 conversion)

---

## ⚡ Installation

1. **Clone this repository**:
   ```bash
   git clone ithub.com/xboxhacker/yt-dlp-gui.git
   cd yt-dlp-gui
Install dependencies:

bash
Copy code

pip install yt-dlp
(Optional) Install FFmpeg for MP3 conversion:

Windows: Download from gyan.dev FFmpeg builds, extract, and add bin folder to PATH.
macOS: brew install ffmpeg
Linux: sudo apt install ffmpeg
▶ Usage
Run the script:

bash
Copy code

python youtube_downloader.py
Fields:
YouTube Video URL – Paste the full video link.
Cookies File (optional) – Required for members-only/private videos. Export cookies from your browser as cookies.txt.
Save Location – Choose where files are stored.
Keep Raw Files (-k) – Keeps original .webm/.m4a files.
Audio Only (MP3) – Downloads only audio and converts to MP3.
🔑 Downloading Members-Only Videos
Install a browser extension like Get cookies.txt.
Login to YouTube, go to the members-only video page.
Export cookies as cookies.txt.
Select it in the app before downloading.
⚠ Notes
Without FFmpeg, MP3 conversion will not be available (audio will remain in its original format).
Downloading copyrighted material without permission may violate YouTube's terms of service.
📜 License
This project is licensed under the MIT License — see the LICENSE file for details.

💡 Credits
yt-dlp – The core downloader backend
FFmpeg – Media processing
Copy code


---

I can also make you a **GitHub-ready repository structure** with:
/youtube-downloader ├── youtube_downloader.py ├── README.md ├── LICENSE └── requirements.txt

Copy code

and fill in `requirements.txt` with:
yt-dlp

Copy code


Do you want me to set that up so you can just push it to GitHub instantly? That way your README, code, and dependencies are all ready to go.


# yt-dlp-gui
Simple Python GUI YouTube Downloader
