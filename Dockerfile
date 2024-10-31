# Use the official Python image as a base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache for dependencies
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the Streamlit port and expose it
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
