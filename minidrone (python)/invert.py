import cv2
import os
folder_path=r"path"
for filename in os.listdir(folder_path):
    if filename.endswith('.tif'):
        image_path=os.path.join(folder_path, filename)
        img=cv2.imread(image_path)
        if img is None:
            print(f"Failed to load image: {filename}")
            continue
        rotated_img=cv2.rotate(img, cv2.ROTATE_180)
        cv2.imwrite(image_path,rotated_img)
