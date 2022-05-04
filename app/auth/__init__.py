from flask import Blueprint, render_template, request, session, redirect, url_for
from app.forms import SignUpForm, SignInForm
from app.models import User, db

main = Blueprint('auth', __name__)

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    signupform = SignUpForm(request.form)
    if request.method = "POST":
        register_user = User(signupform.username, signupform.password)
        db.session.add(register_user)
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("register.html", signupform = signupform)

@auth.route("/signin", methods=["GET", "POST"])
def signin()
    signinform = SignInForm()
    if request.method = "POST":
        login_username = signinform.username.data
        login_user = User.query.filter_by(username=login_username).first()
        if login_user.password == signinform.password.data:
            current_user = login_user
            session["current_user"] = current_user
            session["user_available"] = True
            return redirect(url_for("main.index"))
    return render_template("login.html", signinform=signinform)

