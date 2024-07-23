from flask import render_template
from source import app


# Import HTML files & Creates specific title for every Pages

@app.route("/")
def home():
    return render_template('home.html', title='Homepage')


@app.route("/about")
def about():
    return render_template('about.html', title='About Us')


@app.route("/donate")
def donate():
    return render_template('donate.html', title='Donate')


@app.route("/contact-us")
def contact():
    return render_template('contact.html', title='Contact Us')
