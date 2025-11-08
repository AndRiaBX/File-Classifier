import os
import shutil

thefolder = r"C:\Users\User\OneDrive\Desktop\pythontraining"


dogfolder = os.path.join(thefolder, "dog")
catfolder = os.path.join(thefolder, "cat")

os.makedirs(dogfolder, exist_ok=True)
os.makedirs(catfolder, exist_ok=True)

for file in os.listdir(thefolder):
    file_path = os.path.join(thefolder, file)
    if file.startswith("dog"):
        shutil.move(file_path, dogfolder)
    elif file.startswith("cat"):
        shutil.move(file_path, catfolder)

print("done")
