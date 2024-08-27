
import os
import shutil
import math
parentdir=r"path"
for dir in os.listdir(parentdir):
    srcdir=os.path.join(parentdir,dir)
    destdir=os.path.join(srcdir,r'_')
    images=[f for f in os.listdir(srcdir) if f.endswith(('tiff','.tif','.jpg','.png','.jpeg','.bmp')) and f.split('.')[0].isdigit() and int(f.split('.')[0]) % 2 == 0]
    images.sort(key=lambda x: int(x.split('.')[0]))
    total_images=len(images)
    last15percentcount=math.ceil(0.22 * total_images)
    selected_images=images[-last15percentcount:]
    os.makedirs(destdir, exist_ok=True)
    for image in selected_images:
        src_file=os.path.join(srcdir, image)
        filename,extension=os.path.splitext(image)
        dest_file=os.path.join(destdir,f"{filename}_ {extension}")
        shutil.copy(src_file,dest_file)
    