from flask import Flask, render_template
import os
from pymongo import MongoClient

MONGODB_URI = 'mongodb+srv://himanshu:him12345@cluster0.z9357pa.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(MONGODB_URI)

# create a database

# db = client.python_workshop

# create a collection and insert document
# db.students.insert_one({'name': 'Abhinav','Country':'India', 'age': 20})

# multiple documents/rows
# l = [
#     {'name': 'Ravi','Country':'India', 'age': 20},
#     {'name': 'Brian','Country':'India', 'age': 20},
#     {'name': 'Vinod','Country':'India', 'age': 20}
# ]

# for i in l:
#     db.students.insert_one(i)

#  read values from database
db = client.python_workshop
# s = db.students.find_one({'name':'Abhinav'})

query = {
    'country':'India'
}

s = db.students.find(query)
print(type(s))
for i in s:
    print(i)

# print(client.list_database_names())

app = Flask(__name__)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)