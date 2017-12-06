import unittest
from .models import movie

Movie = movie.Movie

class MovieTest(unittest.testCase):
    '''
    Test Class to test the behaviour of the movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','https://developers.themoviedb.org/3/getting-started/images/khsjha27hbs',)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

if__name__ == '__main__':
    unittest.main()
