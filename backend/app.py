from flask import Flask, request, jsonify, send_from_directory
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder=".")

# MongoDB connection
mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    raise Exception("MONGO_URI is missing!")

client = MongoClient(mongo_uri)
db = client["nilesh_db"]
todos = db["todos"]

# Serve To-Do page
@app.route("/")
def home():
    return send_from_directory(".", "todo.html")

# API to submit todo
@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({"error": "All fields required"}), 400

    todos.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return jsonify({"message": "To-Do item saved successfully"}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
