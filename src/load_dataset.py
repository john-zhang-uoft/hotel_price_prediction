import os
import pandas as pd
import torch
from torch.utils.data import Dataset
import json
  
class Hotel_Dataset(Dataset):
    def __init__(self, path_to_data_dir, transform=None, target_transform=None):
        self.data_dir = path_to_data_dir
        self.transform = transform
        self.target_transform = target_transform

        combined_data = []
        combined_labels = []

        for filename in os.listdir(self.data_dir):
            f = os.path.join(self.data_dir, filename)
            # checking if it is a file
            if os.path.isfile(f):
                f = open('data.json')
                data = json.load(f)
                processed_data, label = processed_data(data)
                combined_data += processed_data
                combined_labels += combined_labels
        
        self.data = combined_data
        self.labels = combined_labels
        
    def process_data(self, data):
        # make sure to add city into the processed data
        processed_data = []
        label = 0
        return processed_data, label

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        data = self.data[idx, :]
        label = self.labels[idx]
        if self.transform:
            image = self.transform(data)
        if self.target_transform:
            label = self.target_transform(label)
        return data, label