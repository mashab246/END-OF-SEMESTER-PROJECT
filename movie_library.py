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
        movie_number = (f"Movie number: {random.randint(1000, 9999)}")
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
    
    def search_and_display_movie(movie_number=None, title=None, actors=None, genre=None, release_date=None):
    # Search by movie number
     if movie_number:
       if movie_number in movies:
           print("\n--- Movie Found ---")
           print_movie_details(movie_number)
       else:
            print("Movie not found!")
       return