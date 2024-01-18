"""
Moves highest bitrate songs from source folder to destination folder.
"""

from pathlib import Path

# Define the source and destination folders
# SOURCE_FOLDER = Path("/Users/timmooren/Music/DJ/Omar")
SOURCE_FOLDER = Path("/Users/timmooren/Music/DJ/MP3s")
DESTINATION_FOLDER = Path("/Users/timmooren/Music/DJ/database_omar")

# Iterate through all subfolders in the source folder
for folder in SOURCE_FOLDER.rglob("*"):
    if folder.is_dir():
        # Iterate through all songs in the subfolder
        for song in folder.iterdir():
            if song.is_file() and song.suffix.lower() in [".mp3", ".flac"]:
                # Get the song's filename and destination path
                filename = song.name
                destination_path = DESTINATION_FOLDER / filename

                # Check if the song already exists in the destination folder
                if destination_path.exists():
                    # Compare the bitrates and keep the one with the highest bitrate
                    existing_song_bitrate = destination_path.stat().st_size
                    new_song_bitrate = song.stat().st_size
                    if new_song_bitrate > existing_song_bitrate:
                        # Move the new song to the destination folder
                        song.replace(destination_path)
                        print(f"Moved file: {song}")
                        print(
                            "Difference in bitrate: ",
                            new_song_bitrate - existing_song_bitrate,
                        )
                else:
                    # Move the song to the destination folder
                    song.replace(destination_path)
                    print(f"Moved file: {song}")
