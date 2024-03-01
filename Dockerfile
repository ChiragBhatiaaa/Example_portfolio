# Base image with Python and Streamlit installed
FROM python:3.9-slim


# Install Python dependencies
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Expose the port for Streamlit
EXPOSE 8501

# Start Streamlit when the container starts
CMD ["streamlit", "run", "main.py"]
