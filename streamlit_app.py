import streamlit as st
import yt_dlp
import os
from pathlib import Path

# Set up default Downloads folder
DOWNLOAD_FOLDER = str(Path.home() / "Downloads")

# Streamlit app UI
st.title('YouTube Video Downloader')
url = st.text_input('Enter YouTube URL')

# Button to trigger video download
if st.button('Download') and url:
    try:
        # Set up yt-dlp options
        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'format': 'best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video info and download
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', 'video')

        video_path = os.path.join(DOWNLOAD_FOLDER, f"{video_title}.mp4")

        # Provide the download link
        st.success(f'Video "{video_title}" downloaded successfully to Downloads folder!')
        st.download_button(
            label="Download Video",
            data=open(video_path, 'rb').read(),
            file_name=f"{video_title}.mp4",
            mime="video/mp4"
        )
    except Exception as e:
        st.error(f"Error: {str(e)}")
