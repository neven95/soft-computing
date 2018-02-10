import torchvision
import torch.nn as nn
import os
import torch
import TransferLearning as tl


theModel = tl.myModel()
theModel = torch.load(tl.PATH)
tl.visualize_model(theModel)