from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User
# from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user, logout_user, login_required
# from ..email import mail_message


@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome to Blogger'

    return render_template('index.html', title=title)
