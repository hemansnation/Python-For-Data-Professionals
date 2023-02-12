from flask import Flask, render_template
import os
import pymongo

MONGODB_URI = 'mongodb+srv://himanshu:him12345@cluster0.z9357pa.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(MONGODB_URI)

print(client.list_Database_names())

app = Flask(__name__)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)