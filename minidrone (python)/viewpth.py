import torch
import numpy as np
import scipy.io as sio
data=torch.load('params.pth',map_location=torch.device('cpu'))
torch.set_printoptions(threshold=float('inf'),precision=7,edgeitems=10)
print(data['fc1.weight'][44,50])
print(data['fc1.weight'].size())