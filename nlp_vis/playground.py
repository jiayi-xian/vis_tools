

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import torch
from transformers import BertTokenizer, BertForSequenceClassification

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased")

inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
#labels = torch.tensor([1]).unsqueeze(0)  # Batch size 1
#outputs = model(**inputs, labels=labels)
print("")


