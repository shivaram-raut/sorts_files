import os
import shutil


# function to move files to the respective folders:
def move(file_type, file_name,  folder_name):
    # creating folder if it doesn't already exist.
    new_folder = os.path.join(path, folder_name)  # path => path provided by user
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

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


# specify the name of the directory to be sorted:
path = input("Enter the path ::")

# making  list of files and folders which are inside  the directory pointed by the path.
contents = os.listdir(path)

for file in contents:
    # moving text files to Notepad(text)
    if ".txt" in file:
        move(".txt", file, "Notepad(text)")

    # moving .exe files to '.exe files'
    elif ".exe" in file:
        move(".exe", file, ".exe files")

    # moving .html files to html
    elif ".html" in file:
        move(".html", file, "html")

    # moving .pdf files to pdf:
    elif ".pdf" in file:
        move(".pdf", file, "pdf")

    # moving .png files to images:
    elif ".png" in file:
        move(".png", file, "images")
    # moving .docx files to 'Ms-word files'
    elif ".docx" in file:
        move(".docx", file,"Ms-word files")

