from pathlib import Path

def move_files():
    """
    Move files from the 'omar_folder' to the 'database_omar_folder' if a corresponding file with the same relative path exists in the database folder and has a larger size.
    """
    omar_folder = Path("/Users/timmooren/Music/DJ/Omar")
    database_omar_folder = Path("/Users/timmooren/Music/DJ/database_omar")

    for search_file in omar_folder.rglob("*"):
        if search_file.is_file():
            relative_path = search_file.relative_to(omar_folder)
            database_file = database_omar_folder / relative_path
            if database_file.exists() and database_file.stat().st_size > search_file.stat().st_size:
                search_file.unlink()
                database_file.rename(omar_folder / relative_path)
                print(f"Moved file: {search_file}")

move_files()
