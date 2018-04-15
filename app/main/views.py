from flask import render_template
from . import main
from .forms import PitchForm


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Welcome to One Minute Pitch'


    return  render_template('index.html', title=title)

@main.route('/pickup', endpoint='pickup')

def pickup():

    '''
    View movie page function that returns the movie details page and its data
    '''

    return render_template('pickup.html')
#
@main.route('/interview', endpoint='interview')

def interview():

    '''
    View movie page function that returns the movie details page and its data
    '''

    return render_template('interview.html')
