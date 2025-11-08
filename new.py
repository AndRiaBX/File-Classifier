
import os
import shutil

# აქ უნდა ჩაწერო ფოლდერის მისამართი
mainfolder = r""
# აქ უნდა ჩაწერო იმ ფოლდერის მისამართი სადაც გინდა შეიქმნას ქვეფოლდერები,
newmainfolder = r"C:\Users\User\OneDrive\Desktop\pythontraining"

newfolder1 = os.path.join(newmainfolder, "new1")  # ვქმნით ახალ ფოლდერს
newfolder2 = os.path.join(newmainfolder, "new2")

os.makedirs(newfolder1, exist_ok=True)  # ვამოწმებთ რომ არსებობს
os.makedirs(newfolder2, exist_ok=True)


for root, dirs, files in os.walk(mainfolder):
    for file in files:
        file_path = os.path.join(root, file)

        if file.startswith(''):  # აქ ჩაწერე ის რაზეც გინდა ფაილი იწყებოდეს
            shutil.move(file_path, newfolder1)
        elif file.startswith(""):  # აქ ჩაწერე ის რაზეც გინდა სხვა ტიპის ფაილი იწყებოდეს
            shutil.move(file_path, newfolder2)

print("done")

