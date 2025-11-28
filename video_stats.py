import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = "MrBeast"

def get_playlist_id():
    url = (
        f"https://youtube.googleapis.com/youtube/v3/channels"
        f"?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        # print(json.dumps(data, indent=4))

        channel_items = data["items"][0]
        playlist_id = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        return playlist_id

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    playlist_id = get_playlist_id()
    print(f"Uploads Playlist ID: {playlist_id}")
    if playlist_id:
        print("Successfully retrieved the playlist ID.")
    else:
        print("Failed to retrieve the playlist ID.")