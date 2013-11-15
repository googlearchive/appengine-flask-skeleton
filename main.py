""" main.py is the top level script.

Return "Hello World" at the root URL.
"""

import os
import sys

# required to load libraries under server/lib that Flask depends on
sys.path.insert(1, os.path.join(os.path.abspath('.'), 'server/lib'))
from flask import Flask
from flask import render_template

app = Flask(__name__.split('.')[0])


@app.route('/')
@app.route('/<name>')
def hello(name=None):
  """ Return hello template at application root URL."""
  return render_template('hello.html', name=name)


