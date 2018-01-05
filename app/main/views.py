from flask import render_template, request, redirect, url_for, abort
from . import main 

@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome to Blogger'

    return render_template('index.html', title=title)
