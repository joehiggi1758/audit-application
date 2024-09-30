# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

COPY . .

# Copy requirements and install dependencies
RUN pip install -r app/requirements.txt

# Expose the port Streamlit uses
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
