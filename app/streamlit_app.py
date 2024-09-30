import streamlit as st
from transformers import pipeline

# Load the Hugging Face question-answering pipeline using DistilBERT
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad", clean_up_tokenization_spaces=True)

# Set up Streamlit app with a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Chat with QA Bot"])

if page == "Overview":
    # Overview Page
    st.title("Welcome to the QA Chatbot App 🤖")
    st.write("""
        This application allows you to interact with a question-answering chatbot. 
        You can enter a context or passage, and then ask questions about it.
        
        ### Features
        - **DistilBERT-based QA**: Uses the DistilBERT model to answer questions.
        - **Interactive Chat**: Engage in a conversation with the QA bot to get answers from a given context.
        
        ### How to Use
        1. Navigate to the "Chat with QA Bot" page using the sidebar.
        2. Enter a context for the bot to understand.
        3. Type in your questions, and the bot will provide the answers.
    """)

elif page == "Chat with QA Bot":
    # Chat Page
    st.title("Chat with QA Bot 🤖")
    st.write("This app allows you to ask questions based on a given context.")

    # Provide a context for questions
    context = st.text_area("Enter the context here:", height=150)

    # Create a chat interface
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Capture user question
    user_question = st.chat_input("Ask a question based on the above context:")

    # Process and display the chat if there's input
    if user_question and context:
        # Get the answer from the QA pipeline
        result = qa_pipeline(question=user_question, context=context)
        answer = result['answer']

        # Update chat history
        st.session_state.chat_history.append(("User", user_question))
        st.session_state.chat_history.append(("AI 🤖", answer))

    # Display chat history with icons
    for role, message in st.session_state.chat_history:
        icon = "🙂" if role == "User" else "🤖"
        st.chat_message(role).write(f"{icon} {message}")
