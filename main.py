import os
import shutil


# function to move files to the respective folders:
def move(file_type, file_name,  folder_name):
    source_path = os.path.join(path, file_name)
    destination_path = os.path.join(path, folder_name, file_name)
    if not os.path.exists(destination_path):
        try:
            shutil.move(source_path, destination_path)
            print(f"File moved to {destination_path}")
        except FileNotFoundError:
            print(f"Source file not found: {source_path} for file type: {file_type}")
        except PermissionError:
            print("Permission denied.")
        except Exception as e:
            print(f"An error occurred: {e}")


# specifying the name of the directory to be sorted:
path = "C:\\Users\\Acer\\Documents_copy\\"

# making  list of files and folders which are inside  the directory pointed by the path.
contents = os.listdir(path)


# creating new folders only if they don't already exist:
folders_name_list = ['images', 'Notepad(text)', '.exe files', 'pdf', 'ms-word', 'html']
for folder in folders_name_list:
    new_folder = os.path.join(path, folder)
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)


for file in contents:
    # moving text files to Notepad(text)
    if ".txt" in file:
        move(".txt", file, "Notepad(text)")

    # moving .exe files to '.exe files'
    if ".exe" in file:
        move(".exe", file, ".exe files")

    # moving .html files to html
    if ".html" in file:
        move(".html", file, "html")

    # moving .pdf files to pdf:
    if ".pdf" in file:
        move(".txt", file, "pdf")

    # moving .png files to images:
    if ".png" in file:
        move(".png", file, "images")

