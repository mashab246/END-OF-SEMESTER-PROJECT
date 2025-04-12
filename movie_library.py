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
   
# Search by other criteria
    found_movies = []
    for m_number, movie in movies.items():
        if (title and title.lower() in movie['title'].lower()) or \
           (actors and any(actor.lower() in [a.lower() for a in movie['actors']] for actor in actors.split(", "))) or \
           (genre and genre.lower() == movie['genre'].lower()) or \
           (release_date and release_date == movie['release_date']):
            found_movies.append(m_number) 
            
    if found_movies:
        print("\n--- Movies Found ---")
        for m_number in found_movies:
            print_movie_details(m_number)
    else:
        print("No movies found matching the criteria.")
        
def print_movie_details(movie_number):
    """Helper function to print movie details."""
    movie = movies[movie_number]
    print(f"Movie Number: {movie_number}")
    print(f"Title: {movie['title']}")
    print(f"Genre: {movie['genre']}")
    print(f"Release Date: {movie['release_date']}")
    print(f"Actors: {', '.join(movie['actors'])}")
    print(f"Description: {movie['description']}")
    print(f"Price: ${movie['price']:.2f}")
    print("--------------------")