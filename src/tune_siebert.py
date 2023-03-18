from transformers import AutoTokenizer, AutoModelForSequenceClassification, AdamW
import torch
from load_dataset import Hotel_Dataset

# Tune siebert on hotel sentiment data

# Load the pre-trained model
model_name = "siebert/sentiment-roberta-large-english"
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Tokenize hotel review dataset
path_to_dir = "./data"
dataset = Hotel_Dataset(path_to_dir, transform=None, target_transform=None)

# 
encoded_reviews = tokenizer(dataset, padding=True, truncation=True, max_length=512, return_tensors='pt')
labels = torch.tensor(dataset)

