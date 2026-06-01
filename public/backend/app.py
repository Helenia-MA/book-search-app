from flask import Flask, request, jsonify
from flask_cors import CORS
from aggregator import search_google_books, search_open_library, combine_data

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Book Search API is running!"

@app.route("/api/search", methods =["GET"])
def search_books():
    title = request.args.get("title", "").strip()
    author = request.args.get("author", "").strip()

    if not title:
        return jsonify([])

    g_results = search_google_books(title, author)
    o_results = search_open_library(title, author)
    result = combine_data(g_results, o_results)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000)