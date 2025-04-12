from datetime import datetime
import random

# In-memory data structures
movies = {}
buyers = {}
sales = {}

# Function to add a movie
def add_movie(title, genre, release_date, actors, description, price):
    # Generate a unique random movie number
    while True:
        movie_number = random.randint(1000, 9999)
        if movie_number not in movies:
            break

    movies[movie_number] = {
        'title': title,
        'genre': genre,
        'release_date': release_date,
        'actors': actors.split(", "),
        'description': description,
        'price': price
    }
    print(f'Movie "{title}" added successfully with Movie Number: {movie_number}!')