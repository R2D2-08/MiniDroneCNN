import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
#120*160*1 pixelated image
#3,605,063 parameters
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
#29,208,649 parameters
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.pool1=nn.MaxPool2d(2,2) 
        self.pool2=nn.MaxPool2d(5,5) 
        self.conv1=nn.Conv2d(1,6,21)
        self.conv2=nn.Conv2d(6,15,21)
        self.conv3=nn.Conv2d(15,24,21)
        self.fc1=nn.Linear(24*21*21,2500) 
        self.fc2=nn.Linear(2500,850)
        self.fc3=nn.Linear(850,280)
        self.fc4=nn.Linear(280,84)
        self.fc5=nn.Linear(84,8)
    def forward(self,x):
        x=self.pool1(F.relu(self.conv1(x)))
        x=self.pool1(F.relu(self.conv2(x)))
        x=self.pool2(F.relu(self.conv3(x)))
        x=x.view(-1,9*21*21)
        x=F.relu(self.fc1(x)) 
        x=F.relu(self.fc2(x))
        x=F.relu(self.fc3(x))
        x=F.relu(self.fc4(x))
        x=self.fc5(x)
        return x