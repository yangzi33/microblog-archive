from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Ziyue"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", user=user, posts=posts)

# the methods arguments indicates that this view function accepts
# GET and POST requests, overriding the default of accepting only
# GET request.
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    # Accept and validte the data submitted by user
    # validate_on_submit: this method does all the form prcesing stuff
    # When the browser sends the GET reques to receive the webpage with
    # the form, this method returns False, so the function skips the if
    # statement and render the template directly
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("index"))

    # Render template
    return render_template("login.html", title = "Sign In", form=form)
