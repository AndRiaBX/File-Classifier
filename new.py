
import os
import shutil

# აქ უნდა ჩაწერო ფოლდერის მისამართი
mainfolder = r"C:\Users\User\OneDrive\Desktop\pythontr2"
newmainfolder = r"C:\Users\User\OneDrive\Desktop\pythontraining"

newfolder1 = os.path.join(newmainfolder, "new1")
newfolder2 = os.path.join(newmainfolder, "new2")

os.makedirs(newfolder1, exist_ok=True)
os.makedirs(newfolder2, exist_ok=True)


for root, dirs, files in os.walk(mainfolder):
    for file in files:
        file_path = os.path.join(root, file)

        if file.startswith('dog'):
            shutil.move(file_path, newfolder1)
        elif file.startswith("cat"):
            shutil.move(file_path, newfolder2)

print("done")
