'''
This python script starts a Flask web application and
displays a text on the screen.

function:
    hello(): Displays a text on the screen
        return - Text

    hbnb(): Displays a text on the screen
        return - Text

    c(text): Displays a text on the screen
        return - Text

    python_(text=none): Displays a text on the screen
        return - Text

    numb(n): Chexks if n is integer
        return - Text
'''

# Import the class Flask from flask module
from flask import Flask
from markupsafe import escape

# Create an instance of Flask class
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''
    A function that returns a text

    return: a text
    '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    A function that returns a text

    return: a text
    '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''
    A function that returns a text

    return: a text
    '''
    text = text.replace('_', " ")
    return "C {}".format(escape(text))


@app.route('/python/(<text>)', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_(text=None):
    '''
    A function that returns a text

    return: a text
    '''
    if text:
        text = text.replace('_', " ")
        return "Python {}".format(text)
    else:
        return "Python is cool"


@app.route('number/<n>', strict_slashes=False)
def numb_(n):
    '''
    Check if n is integer

    Parameter:
        n: the value to check
    return:
        a text
    '''
    if isinstance(n, int):
        return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
