from flask import Flask, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

# from models import 

# CURR_USER_KEY = "curr_user"

app = Flask(__name__)

# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "O0oo0o0o0o0o0o0o0"
toolbar = DebugToolbarExtension(app)

# connect_db(app)



@app.route('/')
def home():
    """Render home page"""

    return render_template('index.html')