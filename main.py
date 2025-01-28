import os
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """Extract the video ID from the YouTube URL."""
    yt = YouTube(url)
    return yt.video_id

def download_transcript(video_id, output_path):
    """Download the transcript and save it to a text file."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        with open(output_path, 'w', encoding='utf-8') as file:
            for line in transcript:
                file.write(f"{line['text']}\n")
        print(f"Transcript saved to {output_path}")
    except Exception as e:
        print(f"Error downloading transcript: {e}")

def main():
    # Input YouTube video URL
    video_url = input("Enter the YouTube video URL: ")

    # Get the video ID
    video_id = get_video_id(video_url)

    # Define the output path on the desktop
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    output_file = os.path.join(desktop_path, f"{video_id}_transcript.txt")

    # Download the transcript
    download_transcript(video_id, output_file)

if __name__ == "__main__":
    main()