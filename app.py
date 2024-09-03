from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('TMDB_API_KEY')
base_url = "https://api.themoviedb.org/3"

app = Flask(__name__)

@app.route('/')
def index():
    url = f"{base_url}/movie/popular"
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'page': 1
    }
    response = requests.get(url, params=params)
    movies = response.json().get('results', []) if response.status_code == 200 else []
    return render_template('index.html', movies=movies)

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    movies = []
    if query:
        url = f"{base_url}/search/movie"
        params = {
            'api_key': api_key,
            'language': 'en-US',
            'query': query,
            'page': 1
        }
        response = requests.get(url, params=params)
        movies = response.json().get('results', []) if response.status_code == 200 else []
    return render_template('search.html', movies=movies, query=query)

if __name__ == "__main__":
    app.run(debug=True)
