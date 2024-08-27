import os
folder_path=r'path'
start_number=1804
file_list=[f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
file_list.sort()
for i, filename in enumerate(file_list, start=start_number):
    file_extension=os.path.splitext(filename)[1]
    new_filename=f"{i}{file_extension}"
    old_file_path=os.path.join(folder_path,filename)
    new_file_path=os.path.join(folder_path,new_filename)
    os.rename(old_file_path, new_file_path)
    print(f"{filename} to {new_filename}")
