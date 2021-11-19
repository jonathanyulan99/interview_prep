# routes are stored here in Views
# webpages the user can navigate too

# BLUEPRINT of our application; URLs defined path(s)
from flask import Blueprint

# doesn't need to be labelled views
# Blueprint('user_variable_name',__name__)
views = Blueprint('views', __name__)

# name of the Blueprint()
# ('/') - homepage defined route

# @-indicates a selector
@views.route('/')
# whenever you hit that route, you execute the home() function
def home():
    return "<h1>HELLO THERE</h1>"

# TEST
@views.route('/Home')
def stuff():
    user = input('What is your Name?')
    return f'Your name is {user}'