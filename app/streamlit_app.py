import streamlit as st

st.title("Insurance Complaint Classifier")

user_input = st.text_area("Enter customer complaint:")

if st.button("Classify"):
    inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=-1).item()

    # Assuming you have a mapping from label numbers to categories
    label_map = {0: "Claims Issue", 1: "Fee Dispute", 2: "Policy Administration"}
    st.write(f"Predicted Category: {label_map[prediction]}")
