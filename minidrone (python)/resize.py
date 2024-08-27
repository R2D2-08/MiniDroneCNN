from PIL import Image
import os
def resize_images(input_folder,output_folder,new_size=(50,50)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  
    for img_name in os.listdir(input_folder):
        img_path=os.path.join(input_folder,img_name)
        if os.path.isfile(img_path):
            with Image.open(img_path) as img:
                img_resized=img.resize(new_size,Image.LANCZOS)
                img_resized.save(os.path.join(output_folder,img_name))
input_folder = r'srcdir' 
output_folder = r'destdir'
resize_images(input_folder,output_folder)
