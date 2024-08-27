import os
import math
parentdir=r"path"
for dir in os.listdir(parentdir):
    srcdir=os.path.join(parentdir, dir)
    images=[f for f in os.listdir(srcdir) if f.endswith(('tiff','.tif','.jpg','.png','.jpeg','.bmp')) and f.split('.')[0].isdigit() and int(f.split('.')[0]) % 2 == 0]
    images.sort(key=lambda x: int(x.split('.')[0]))
    total_images=len(images)
    lass22percentcount=math.ceil(0.22 * total_images)
    selected_images=images[-lass22percentcount:]
    for image in selected_images:
        deletefiles=os.path.join(srcdir, image)
        os.remove(deletefiles)
        print(f"Deleted: {image} from {srcdir}")
