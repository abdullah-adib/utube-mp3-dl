import yt_dlp
import os

def download_youtube_audio(url):
    # Create 'downloaded' folder if it doesn't exist
    download_path = os.path.join(os.getcwd(), 'downloaded')
    os.makedirs(download_path, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'ffmpeg_location': r'C:Your_path\ffmpeg\bin',  # Update this path if needed
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
youtube_url = "https://youtu.be/your_video_url"
download_youtube_audio(youtube_url)