#ctrl+shift+p to make sure that you are running under the right development environment 'Python 3.9.1 32-bit'

# website is a python package
# __init__.py makes everything in that folder where its located a PYTHON package
from website import create_app

# create_app made in our ___init__.py package
app = create_app()

# only runs your main.py file not other files labelled as such
# only if we run this file, not if we import it will we execute this line
# ensures that other __main__ files that are labeled as such are not executed
if __name__ == '__main__':
    # debug=True basically nodemon, keeps running your FLASK server
    app.run(debug=True)
