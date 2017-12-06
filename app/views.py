from flask import render_template
from .requests import get_movies,get_movie
from app import app

#Views
# @app.route('/movies/')
#
# def movie(movie_id):
#     '''
#     View page function that returns the movies details page and its data
#     '''
#     return render_template('movie.html',id = movie_id)

@app.route('/movie/<int:id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'

    return render_template('movie.html',title = title,movie = movie)

@app.route('/')
def index():
    '''
    view root function that return the index page and its data
    '''
    # Getting  movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )
