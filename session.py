from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
app = Flask(__name__)
app.config["SECRET_KEY"] = 'ThisIsASecretKey'
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["user"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("home.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=8082)