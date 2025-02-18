import pymongo
# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Access a database
db = client["mydatabase"]
# Access a collection
collection = db["mycollection"]
 
# Example 1: Insert a single document
document = {"name": "John", "age": 25, "city": "Mumbai"}
collection.insert_one(document)
# Example 2: Insert multiple documents
documents = [
 {"name": "Amit", "age": 30, "city": "Delhi"},
 {"name": "Sara", "age": 22, "city": "Bangalore"}
]
collection.insert_many(documents)
# Example 3: Insert with additional fields
document = {"name": "Emily", "age": 28, "city": "Chennai", "occupation":
"Engineer"}
collection.insert_one(document)
# Read (Retrieve Documents)
# Update (Modify Documents)
# Example 1: Insert a single document
document = {"name": "John", "age": 25, "city": "Mumbai"}
collection.insert_one(document)
# Example 2: Insert multiple documents
documents = [
 {"name": "Amit", "age": 30, "city": "Delhi"},
 {"name": "Sara", "age": 22, "city": "Bangalore"}
]
collection.insert_many(documents)
# Example 3: Insert with additional fields
document = {"name": "Emily", "age": 28, "city": "Chennai", "occupation":
"Engineer"}
collection.insert_one(document)
# Example 1: Retrieve all documents
for doc in collection.find():
 print(doc)
# Example 2: Retrieve documents with a filter
query = {"city": "Mumbai"}
for doc in collection.find(query):
 print(doc)
# Example 3: Retrieve specific fields
for doc in collection.find({}, {"name": 1, "city": 1}):
 print(doc)
# Example 1: Update a single document
query = {"name": "John"}
new_values = {"$set": {"age": 26}}
collection.update_one(query, new_values)
# Example 2: Update multiple documents
query = {"city": "Delhi"}
new_values = {"$set": {"city": "New Delhi"}}
# Delete (Remove Documents)
# 3. Data Manipulation in MongoDB Using Python
# Indexing and Querying with Filters
collection.update_many(query, new_values)
# Example 3: Increment a field value
query = {"name": "Amit"}
new_values = {"$inc": {"age": 1}}
collection.update_one(query, new_values)
# Example 1: Delete a single document
query = {"name": "John"}
collection.delete_one(query)
# Example 2: Delete multiple documents
query = {"city": "New Delhi"}
collection.delete_many(query)
# Example 3: Delete all documents
collection.delete_many({})
# Example 1: Create an index on the "name" field
collection.create_index([("name", pymongo.ASCENDING)])
# Example 2: Query with a filter
query = {"age": {"$gt": 25}}
for doc in collection.find(query):
 print(doc)
# Example 3: Query with multiple conditions
query = {"age": {"$gt": 25}, "city": "Mumbai"}
for doc in collection.find(query):
 print(doc)