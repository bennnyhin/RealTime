import sys
import sqlite3 as lite
from flask import Flask, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

#example how to access database
# con = lite.connect("information.db")
# cur = con.cursor()
# cur.execute("SELECT * FROM information WHERE username='%s'" % username)
# information = cur.fetchall()


@app.route("/")
def index():
    return render_template("index.html", message="hello")

@app.route("/register")
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation_password = request.form.get("confirmation password")

        #error checking
        if not username:
            return redirect("/apology")
        if not password:
            return redirect("/apology")
        if not confirmation_password:
            return redirect("/apology")
        if password != confirmation_password:
            return redirect("/apology")
        

        return render_template("register.html")

@app.route("/task")
def task():
    return render_template("task.html")

@app.route("/apology")
def apology():
    return render_template("apology.html")

if __name__ == "__main__":
    app.run()

