### Overview
#### *By Joey Higgins*

# Question and Answer AI Chatbot 🤖

## Overview
Welcome to the **Question and Answer AI Chatbot** repository! This project showcases an interactive question-answering chatbot designed specifically for internal financial professionals. By utilizing a machine learning model, this app helps associates interactively query documents, making it easier to extract insights from financial reports and manuals, improving productivity, and speeding up financial processes.

This project leverages modern AI technologies, including Hugging Face Transformers, and showcases practical software engineering skills, including Python development, containerization, and deployment on Linux environments.

## Features
- **Interactive QA Chatbot**: Ask questions about a given financial document or passage, and get accurate responses in real time.
- **Powered by DistilBERT**: Uses the DistilBERT model for efficient and extractive question answering.
- **Web Interface**: Developed using Streamlit, allowing easy access and an intuitive chat-like interface.
- **Deployment Flexibility**: Designed to run seamlessly on Linux servers, making it easy to integrate into existing infrastructure.

## Technologies Used
- **Python**: The main programming language used for development.
- **Hugging Face Transformers**: For utilizing pre-trained NLP models.
- **Streamlit**: For creating a user-friendly web application.
- **Linux**: Configured for server-side deployment, leveraging bash scripting for automation and orchestration.

## Usage
- **Overview Page**: Provides an introduction and explanation of how the app works.
- **Chat with QA Bot Page**: Enter an financial document or passage as context, and interact with the chatbot by asking relevant questions.

## Project Structure
- **app.py**: Main Streamlit application file.
- **Dockerfile**: Contains the instructions to containerize the application.
- **requirements.txt**: Lists all the Python dependencies required for the project.
- **README.md**: This file, containing the project documentation.

### Key Applications
#### Anti-Money Laundering (AML)
- **Speeding up KYC Analysis**: In AML, analysts often need to review large volumes of customer information and documents during the Know Your Customer (KYC) process. This QA tool can help quickly extract key information from these documents, speeding up the review and decision-making process.
- **Identifying Red Flags**: QA models can assist in identifying specific patterns or red flags in customer behavior based on large datasets, allowing analysts to focus on high-risk cases.

#### Digital Internal Audit
- **Efficient Documentation Review**: Internal audits often require the review of extensive documentation, policies, and procedures. This QA tool can significantly reduce the time required to extract relevant information from these documents, ensuring that associates can focus on analysis rather than manual document searches.
- **Improved Audit Insights**: By asking targeted questions, associates can use the QA tool to quickly gain insights into compliance issues, control weaknesses, and operational risks, allowing for more efficient and effective audits.

#### Other
- **Compliance Checks**: Quickly get answers about policy compliance by querying related sections of regulatory documents.
- **Training and Knowledge Sharing**: Use the chatbot for training junior associates by providing instant access to critical insights from various documents.

## Deployment
This application is designed for easy deployment in a cloud or on-premises environment using Linux. The containerized nature ensures consistent performance and ease of scalability, it also ensures data privacy as data isn't used to retrain the base model and doesn't leave the application.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
If you have any questions or suggestions, feel free to contact me at joehiggi1758@gmail.com. You can also connect with me on [LinkedIn](https://linkedin.com/in/josephpmhiggins).
