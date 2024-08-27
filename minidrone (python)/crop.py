import cv2
import os
source_dir=r"src path"
destination_dir=r"dest path"
os.makedirs(destination_dir, exist_ok=True)
for filename in os.listdir(source_dir):
    img_path=os.path.join(source_dir, filename)
    img=cv2.imread(img_path)
    if img is None:
        print(f"Failed to load {filename}")
        continue
    x=30
    y=10
    w=160-60 
    h=120-20 
    cropped_img=img[y:y+h,x:x+w]
    dest_img_path=os.path.join(destination_dir,f"{filename}")
    cv2.imwrite(dest_img_path,cropped_img)

