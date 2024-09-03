import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('TMDB_API_KEY')

base_url = "https://api.themoviedb.org/3"

def get_popular_movies():
    url = f"{base_url}/movie/popular"
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'page': 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        movies = response.json().get('results', [])
        for movie in movies:
            print(f"Title: {movie['title']}, Release Date: {movie['release_date']}")
    else:
        print("Failed to retrieve data:", response.status_code)
        
def search_movies(query):
    """Pretražuje filmove prema unetim ključnim rečima."""
    url = f"{base_url}/search/movie"
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'query': query,
        'page': 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        movies = response.json().get('results', [])
        if not movies:
            print("No movies found with the given query.")
        for movie in movies:
            print(f"Title: {movie['title']}, Release Date: {movie['release_date']}")
    else:
        print("Failed to retrieve data:", response.status_code)


if __name__ == "__main__":
    print("Choose an option:")
    print("1. View popular movies")
    print("2. Search movies by keyword")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        get_popular_movies()
    elif choice == "2":
        query = input("Enter a keyword to search for movies: ")
        search_movies(query)
    else:
        print("Invalid choice. Please enter 1 or 2.")

