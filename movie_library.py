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
    
# Function to sell a movie
def sale_movie(movie_number, copies_sold, buyer_name, buyer_gender, buyer_contact):
    # Check if the movie exists
    if movie_number not in movies:
        print("Movie not found!")
        return

    # Check if the buyer already exists, otherwise register them
    buyer_number = None
    for b_number, buyer in buyers.items():
        if buyer['name'] == buyer_name and buyer['contact'] == buyer_contact:
            buyer_number = b_number
            break

    if not buyer_number:
        # Generate a unique random buyer number
        while True:
            buyer_number = random.randint(1000, 9999)
            if buyer_number not in buyers:
                break
        
        buyers[buyer_number] = {
            'name': buyer_name,
            'gender': buyer_gender,
            'contact': buyer_contact
        }
        print(f'Buyer "{buyer_name}" registered successfully with Buyer Number: {buyer_number}!')

    # Generate a unique random receipt number
    while True:
        receipt_number = random.randint(1000, 9999)
        if receipt_number not in sales:
            break
        
     # Record the sale
    movie = movies[movie_number]
    total_price = movie['price'] * copies_sold
    sale_date = datetime.now().strftime('%Y-%m-%d')

    sales[receipt_number] = {
        'sale_date': sale_date,
        'movie_number': movie_number,
        'copies_sold': copies_sold,
        'total_price': total_price,
        'member_number': buyer_number
    }

    print(f'Sale recorded successfully! Receipt Number: {receipt_number}, Total Price: ${total_price:.2f}')