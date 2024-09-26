import os
import shutil

def rename_files(directory, backup_directory):
    # Create a list of all files in the directory with .mp4 extension
    files = [file for file in os.listdir(directory) if file.endswith('.mp4')]

    # Make a copy of each file to the backup directory
    for file in files:
        file_path = os.path.join(directory, file)
        backup_path = os.path.join(backup_directory, file)
        shutil.copy2(file_path, backup_path)

    # Rename all the files with an increasing number
    for i, file in enumerate(files):
        file_path = os.path.join(directory, file)
        new_file_name = f"{i+1}.mp4"
        new_file_path = os.path.join(directory, new_file_name)
        os.rename(file_path, new_file_path)

# Example usage
directory = input("Enter the directory path: ")
backup_directory = input("Enter the backup directory path: ")
rename_files(directory, backup_directory)