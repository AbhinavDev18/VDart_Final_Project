from pymongo import MongoClient
import os

# Your MongoDB connection string
MONGO_URI = os.environ['MONGO_URI']

# Initialize client
client = MongoClient(MONGO_URI)

# Access your database
db = client['Feedback']

# Access a collection (like a table)
feedback_collection = db['feedback']  # Replace 'feedback' with your collection name
