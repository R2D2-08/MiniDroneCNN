import os
import shutil
parentdir=r"parentdir"
destdir=r"destdir"
os.makedirs(destdir, exist_ok=True)
for folder_name in os.listdir(parentdir):
    folder_path=os.path.join(parentdir, folder_name)
    if os.path.isdir(folder_path):
        subfolder_path=os.path.join(folder_path, '_')
        if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
            new_folder_name=folder_name
            new_folder_path=os.path.join('_', new_folder_name)
            final_destination=os.path.join(destdir, new_folder_name)
            shutil.move(subfolder_path, final_destination)            
