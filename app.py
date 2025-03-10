from flask import Flask, render_template, url_for, redirect, flash
from form import SignupForm, Loginform


app = Flask(__name__)
app.config["SECRET_KEY"] = "this_is_a_secret_key"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f"Successfully Registered {form.username.data}!")
        return redirect(url_for("home"))
    return render_template("signup.html", title="Singup", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = Loginform()
    if form.validate_on_submit():
        flash(f"Login is Successfully and ready to use  {form.email.data}!")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)