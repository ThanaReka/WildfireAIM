# Step 1: Set up the Flask application and required imports
from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

# Step 2: Define the function to load and search wildfire Q&A data from data.json
def load_wildfire_data(search_query=None):
    if not search_query:  # Return empty list if no search query is provided
        return []
    try:
        with open('backend/data/data.json', 'r') as file:
            data = json.load(file)
        # Perform exact match (case-insensitive) on the question field
        search_query = search_query.lower().strip()
        for item in data:
            if search_query == item.get('question', '').lower().strip():
                return [item]  # Return single matching item as a list
        return []  # No match found
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Step 3: Define the main route to render the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    search_query = ''
    if request.method == 'POST':
        search_query = request.form.get('search', '')
        results = load_wildfire_data(search_query)
    return render_template('index.html', results=results, search_query=search_query)

# Step 4: Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)