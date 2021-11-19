from flask import Blueprint

# authentication Blueprint
auth = Blueprint('auth', __name__)

# thus it would be website_name/Hello
# @auth.route("Hello")

# 1st Selector to .route("/webpage_title_page_name"
# This is routing from a Blueprint

@auth.route("authorization")
def authorization():
    return "<p>THIS IS THE AUTHENTICATION PAGE</p>"


@auth.route("/login")
# 2nd define the function
# usually same as the /filepath
def login():
    return "<p>You've Logged In</p>"

# 2nd selector; identified with @ sign
# BLUEPRINT('auth',__name__) = user_variable_name.route("/trailing_web_page_title")


@auth.route("/logout")
def logout():
    return "<p>You've Logged Out</p>"

# 3rd @selector.route("/webpage")


@auth.route("/sign-up")
def sign_up():
    return "<p>SIGN UP</p>"
