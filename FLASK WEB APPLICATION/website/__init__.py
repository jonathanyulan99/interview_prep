# Make this main 'Website' folder a python package

from flask import Flask


def create_app():
    # __name__ represents the name of the file that was read
    app = Flask(__name__)
    # secret_key variable to store password literal
    app.config['SECRET_KEY'] = 'Jonathan1990!!'

    # WE HAVE SOME BLUEPRINTS, show where they are
    # here you will need to import your .py files
    from .views import views
    from .auth import auth

    # now register them with our flask application
    # FLASK(__name__).register_blueprint(imported_variable,url_prefix="/theroute")
    # url_prefix /
    # url_prefix /
    # having this loaded as such ensures that the routes always have that prefix listed first and foremost /
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    # app.register_blueprint(views,url_prefix='/Home')
    return app
