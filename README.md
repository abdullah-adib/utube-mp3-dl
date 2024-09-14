# YouTube Audio Downloader

This Python script allows you to download the audio from YouTube videos as MP3 files and save them in a 'downloaded' folder.

## Features

- Downloads audio from YouTube videos
- Converts the audio to MP3 format
- Uses the highest quality audio available
- Creates a 'downloaded' folder to store the audio files

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed
- pip (Python package installer)
- FFmpeg installed and added to your system PATH

## Installation

1. Clone this repository or download the script.

2. Install the required Python package:

   ```
   pip install yt-dlp
   ```

3. Install FFmpeg:
   - Download FFmpeg from the [official website](https://ffmpeg.org/download.html)
   - Extract the archive to a location on your computer (e.g., `C:\ffmpeg`)
   - Add the `bin` folder of FFmpeg to your system PATH:
     - Right-click on 'This PC' or 'My Computer' and select 'Properties'
     - Click on 'Advanced system settings'
     - Click on 'Environment Variables'
     - Under 'System variables', find and select 'Path', then click 'Edit'
     - Click 'New' and add the path to the FFmpeg bin folder (e.g., `C:\ffmpeg\bin`)
     - Click 'OK' to close all dialogs

## Usage

1. Open the script `dl.py` in a text editor.

2. Modify the `youtube_url` variable with the URL of the YouTube video you want to download:

   ```python
   youtube_url = "https://youtu.be/your_video_id"
   ```

3. Run the script:

   ```
   python dl.py
   ```

   The script will create a 'downloaded' folder in the same directory as the script (if it doesn't already exist) and save the downloaded MP3 file there.

## Troubleshooting

If you encounter an error related to FFmpeg not being found, you can specify the FFmpeg location in the script:

1. Open `dl.py` in a text editor.
2. Locate the `ydl_opts` dictionary.
3. Update the `ffmpeg_location` line with your actual FFmpeg location:

   ```python
   'ffmpeg_location': r'C:\path\to\ffmpeg\bin\ffmpeg.exe',
   ```

## Legal Note

Please ensure you have the right to download and use the content. Respect copyright laws and YouTube's terms of service.

## License

This project is open source and available under the [MIT License](LICENSE).