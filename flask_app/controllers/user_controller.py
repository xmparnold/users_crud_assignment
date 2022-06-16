from flask_app import app
from flask import session, render_template, request, redirect
from flask_app.models.user_model import User

@app.route( "/" )
@app.route( "/home")
@app.route( "/all_users")
def display_users():
    list_users = User.get_all()
    return render_template( "index.html", list_users = list_users )

@app.route( "/newuser" )
def display_new_user_form():
    return render_template( "newUser.html" )

@app.route( "/newuser", methods = [ 'POST' ] )
def create_new_user():
    User.create( request.form )
    return redirect( "/home" )