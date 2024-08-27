import torch
import scipy.io as sio
data=torch.load('params.pth',map_location=torch.device('cpu'))
modifieddata={}
for key in data:
    new_key=key.replace('.','_')  
    modifieddata[new_key]=data[key].numpy() if isinstance(data[key], torch.Tensor) else data[key]
sio.savemat('params.mat',modifieddata)