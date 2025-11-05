from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

YELP_API_KEY = os.getenv("YELP_API_KEY")
YELP_API_URL = "https://api.yelp.com/v3/businesses/search"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    location = request.form.get("location")
    headers = {"Authorization": f"Bearer {YELP_API_KEY}"}
    params = {"term": "food", "location": location, "limit": 50}

    response = requests.get(YELP_API_URL, headers=headers, params=params)
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)