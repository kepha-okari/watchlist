from flask import render_template
from .request import get_movies
from app import app

#Views
@app.route('/movies/')

def movie(movie_id):
    '''
    View page function that returns the movies details page and its data
    '''
    return render_template('movie.html',id = movie_id)

@app.route('/')
def index():
    '''
    view root function that return the index page and its data
    '''
    # Getting popula000000000000r movie
    popular_movies = get_movies('popular')
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, popular = popular_movies)
