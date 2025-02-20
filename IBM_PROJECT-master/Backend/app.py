from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)
PORT = int(os.getenv("PORT", 5000))

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/mydatabase")  # Default local DB if not set
try:
    client = MongoClient(MONGO_URI)
    db = client.get_database()  # Get database reference
    print("Connected to MongoDB")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

@app.route('/')
def home():
    return "Hello from Backend!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
