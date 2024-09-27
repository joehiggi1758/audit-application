import streamlit as st
# from model import classify_audit_procedure

# Streamlit app
st.title("Audit Procedure Automation Classifier")

# Input for audit procedure text
procedure_text = st.text_area("Enter the audit procedure text:")

if st.button("Classify"):
    if procedure_text:
        result = classify_audit_procedure(procedure_text)
        if result == 1:
            st.success("This audit procedure is a good candidate for automation!")
        else:
            st.warning("This audit procedure is NOT a good candidate for automation.")
    else:
        st.error("Please enter some text to classify.")
