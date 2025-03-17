import re
import numpy as np
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')

def preprocess_text(text):
    # Clean text: Remove URLs, special characters, and extra spaces
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    # Tokenize for BERT model
    encoded = tokenizer.encode_plus(
        text,
        max_length=128,
        truncation=True,
        padding='max_length',
        return_tensors='tf'
    )
    return np.array(encoded['input_ids'])