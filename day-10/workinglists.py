import os

folders = input("please provide list of folders names with spaces in between:").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide a folder name, looks like this doesn't exists:" + folder)
        break
    except PermissionError:
        break
        print("No access to this folder:" + folder)
    
    print(" === listing files for the folder - " + folder)
    for file in files:
        print(file)

