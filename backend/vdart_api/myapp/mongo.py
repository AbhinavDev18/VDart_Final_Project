from pymongo import MongoClient

# Your MongoDB connection string
MONGO_URI = "mongodb+srv://abhinav1:abhinav118@cluster0.8vyve.mongodb.net/Feedback?retryWrites=true&w=majority"

# Initialize client
client = MongoClient(MONGO_URI)

# Access your database
db = client['Feedback']

# Access a collection (like a table)
feedback_collection = db['feedback']  # Replace 'feedback' with your collection name
