import os
import shutil
parent=r"path"
filecount=0
for folder_name in os.listdir(parent):
    folder_path=os.path.join(parent,folder_name)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            file_path=os.path.join(folder_path,file_name)
            if os.path.isdir(file_path):
                continue
            new_file_name=f"{filecount}{os.path.splitext(file_name)[1]}"
            new_file_path=os.path.join(parent,new_file_name)
            shutil.move(file_path,new_file_path)
            filecount+=1
for folder_name in os.listdir(parent):
    folder_path=os.path.join(parent,folder_name)
    if os.path.isdir(folder_path):
        os.rmdir(folder_path)