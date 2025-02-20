# Use an official Python image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy project files
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend code
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "cicd.py", "--server.port=8501", "--server.address=0.0.0.0"]