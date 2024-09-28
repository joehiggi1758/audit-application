import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import Trainer, TrainingArguments
import torch
from torch.utils.data import DataLoader, Dataset
import pickle
import os

# Load FinBERT model and tokenizer
model_name = "yiyanghkust/finbert-tone"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Check if the model is already pickled, if yes, load it
model_path = './finbert_trained_model.pkl'

if os.path.exists(model_path):
    print("Loading pickled model...")
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
else:
    print("Training a new model...")
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Load data (assuming CFPB dataset downloaded as 'complaints.csv')
    df = pd.read_csv('../data/complaints.csv')

    # Filter for insurance-related complaints
    insurance_data = df[df['product'].str.contains('Insurance', na=False)]

    # Extract relevant columns
    texts = insurance_data['complaint_what_happened'].fillna('')

    # Tokenize the data
    inputs = tokenizer(texts.tolist(), padding=True, truncation=True, return_tensors="pt")

    class ComplaintsDataset(Dataset):
        def __init__(self, encodings, labels):
            self.encodings = encodings
            self.labels = labels

        def __getitem__(self, idx):
            item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
            item['labels'] = torch.tensor(self.labels[idx])
            return item

        def __len__(self):
            return len(self.labels)

    # Assuming you have labeled your data into categories (0, 1, 2, ...)
    labels = insurance_data['issue_category'].astype(int).tolist()  # Replace with your labels
    dataset = ComplaintsDataset(inputs, labels)
    dataloader = DataLoader(dataset, batch_size=8, shuffle=True)

    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=3,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=16,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset
    )

    trainer.train()

    # Save the model to a pickle file after training
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

print("Model is ready for inference.")
