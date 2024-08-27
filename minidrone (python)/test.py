import numpy as np
import os
import cv2
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
class dataset(Dataset):
    def __init__(self,images,labels):
        self.image=images
        self.label=labels
    def __len__(self):
        return len(self.image)
    def __getitem__(self,id):
        sample={'image':self.image[id],'label':self.label[id]}
        return sample
#arrays of images and labels
#the array of the labels is simply the name of the folders ordered up in a line and fed to the build_arrays function
#the array of the images on the other hand, one function to retrieve the pixels and another to append the pixels to an array
images=[]
labels=[]
def retrieve_pixels(path):
    img=cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    pixels=np.expand_dims(img,axis=0)
    return pixels
def build_arrays(folder):
    for file in os.listdir(folder):
        folder_path=os.path.join(folder,file)
        for img_name in os.listdir(folder_path):
            img_path=os.path.join(folder_path,img_name)
            pxls=retrieve_pixels(img_path)
            images.append(pxls)
            x=np.zeros(5)
            x[int(file)]=1
            labels.append(x)
    return images,labels
images,labels=build_arrays(r'path')
images=np.array(images)
labels=np.array(labels)
images=torch.tensor(images,dtype=torch.float32)
labels=torch.tensor(labels,dtype=torch.float32)
dronedataset=dataset(images=images,labels=labels)
traindata=DataLoader(dronedataset,batch_size=32,shuffle=2)
model=Net()
criterion=nn.CrossEntropyLoss()
optimizer=optim.SGD(model.parameters(),lr=0.001,momentum=0.9)
for epoch in range(5): 
    current_loss=.0
    for i,data in enumerate(traindata,0):
        imagess=data['image']
        labelss=data['label']
        optimizer.zero_grad()
        outputs=model(imagess)
        loss=criterion(outputs,labelss)
        loss.backward()
        optimizer.step()
        current_loss+=loss.item()
        if i%10==0:
            print(f'[{epoch+1}, {i+1}] loss: {current_loss:.4f}')
        current_loss=.0
torch.save(model.state_dict(),'params.pth')