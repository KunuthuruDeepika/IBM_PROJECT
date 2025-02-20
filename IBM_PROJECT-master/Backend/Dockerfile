# Use Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# Expose backend API port (e.g., FastAPI/Flask)
EXPOSE 5000

# Run the backend server
CMD ["python", "app.py"]