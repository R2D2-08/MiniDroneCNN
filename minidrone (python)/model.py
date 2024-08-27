import numpy as np
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
        self.conv1=nn.Conv2d(1,3,21)  
        self.pool=nn.MaxPool2d(2,2) 
        self.conv2=nn.Conv2d(3,9,21)
        self.fc1=nn.Linear(9*21*21,1000) 
        self.fc2=nn.Linear(1000,200)
        self.fc3=nn.Linear(200,80)
        self.fc4=nn.Linear(80,8)
    def forward(self,x):
        x=self.pool(F.relu(self.conv1(x)))
        x=self.pool(F.relu(self.conv2(x)))
        x=x.view(-1,9*21*21)
        x=F.relu(self.fc1(x)) 
        x=F.relu(self.fc2(x))
        x=F.relu(self.fc3(x))
        x=self.fc4(x)
        return x
class dataset(Dataset):
    def __init__(self,images,labels):
        self.image=images
        self.label=labels
    def __len__(self):
        return len(self.images)
    def __getitem__(self,id):
        sample={'image':self.images[id],'label':self.labels[id]}
        return sample
#arrays of images and labels
#the array of the labels is simply the name of the folders ordered up in a line and fed to the build_arrays function
#the array of the images on the other hand, one function to retrieve the pixels and another to append the pixels to an array
images=[]
labels=[]
def retrieve_pixels(path):
    with Image.open(path) as img:
        img = img.convert('RGB')
        pixels = np.array(img)
    return pixels
def build_arrays(folder):
    for file in os.listdir(folder):
        folder_path=os.path.join(folder,file)
        for img_name in os.listdir(folder_path):
            img_path=os.path.join(folder_path,img_name)
            pxls=retrieve_pixels(img_path)
            images.append(pxls)
            labels.append(file)
    return images,labels
dronedataset=dataset(build_arrays('images'))    
traindata=DataLoader(dronedataset,batch_size=32,shuffle=2)
model=Net()
criterion=nn.CrossEntropyLoss()
optimizer=optim.SGD(model.parameters(),lr=0.001,momentum=0.9)
for epoch in range(): 
    current_loss=.0
    for i,data in enumerate(traindata,0):
        inputs, labels=data
        optimizer.zero_grad()
        outputs=model(inputs)
        loss=criterion(outputs,labels)
        loss.backward()
        optimizer.step()
        current_loss+=loss.item()
        print(f'[{epoch+1}, {i+1}] loss: {current_loss:.3f}')
        current_loss=.0
torch.save(model.state_dict(),'params.pth')