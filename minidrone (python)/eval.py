import numpy as np
import cv2
import os
from PIL import Image
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1=nn.Conv2d(1,6,11)  
        self.pool=nn.MaxPool2d(2,2) 
        self.conv2=nn.Conv2d(6,18,11)
        self.fc1=nn.Linear(5*5*18,84)
        self.fc2=nn.Linear(84,5)
    def forward(self,x):
        x=self.pool(F.relu(self.conv1(x)))
        x=self.pool(F.relu(self.conv2(x)))
        x=x.view(-1,5*5*18)
        x=F.relu(self.fc1(x))
        x=F.softmax(self.fc2(x))
        return x
def retrieve_pixels(path):
    img=cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    pixels=np.expand_dims(img,axis=0)
    return pixels
image=retrieve_pixels(r'path')
image=np.array(image)
image=torch.tensor(image,dtype=torch.float64)
model=Net().double()
model.eval()
model.load_state_dict(torch.load(r'path'))
with torch.no_grad():
    output=model(image)
    print(output)
total_params = sum(p.numel() for p in model.parameters())
print(total_params)




#tensor([[ 46.5350,  -3.6824, -14.6894, -13.0334,   5.2222,   5.4272,  -8.5911,
#      -6.5785]])
#tensor([[ 46.4466,  -3.6564, -14.6510, -13.0558,   5.2215,   5.4009,  -8.5743,
#      -6.5847]])
