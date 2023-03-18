from transformers import AutoTokenizer, AutoModelForSequenceClassification, AdamW
import torch

# Load the pre-trained model
model_name = "siebert/sentiment-roberta-large-english"
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)


