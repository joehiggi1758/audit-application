import torch
from transformers import LlamaTokenizer, LlamaForSequenceClassification

# Load the tokenizer and model
tokenizer = LlamaTokenizer.from_pretrained("huggingface/llama-3")
model = LlamaForSequenceClassification.from_pretrained("huggingface/llama-3")

# Move the model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def classify_audit_procedure(procedure_text):
    inputs = tokenizer(procedure_text, return_tensors="pt", padding=True, truncation=True).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    predicted_class = torch.argmax(outputs.logits, dim=-1).item()
    return predicted_class  # Returns 0 or 1 (automation candidate or not)
