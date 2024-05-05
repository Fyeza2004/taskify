import re
import os
import math
import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, logout_required

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'task_manager'

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///tasks.db")

@app.route("/")
@login_required
def index():
    username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]["username"]
    tasks = db.execute("SELECT id, title, description, strftime('%m-%d-%Y', starting_date) AS formatted_starting_date, strftime('%m-%d-%Y', due_date) AS formatted_due_date FROM tasks WHERE username_id = ? ORDER BY due_date NULLS LAST, starting_date;", session["user_id"])
    for task in tasks:
        due_date = task["formatted_due_date"]
        task["status"] = True
        if due_date:
            due_date_format = datetime.datetime.strptime(due_date, "%m-%d-%Y")
            current_date = datetime.datetime.now()
            task["status"] = True if ((due_date_format - current_date).days >= 0) else False

    return render_template("index.html", username=username, tasks=tasks)


@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/")


@app.route("/signup", methods=["GET", "POST"])
@logout_required
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            error_message = "You must provide a username!!!"
            return render_template('error_message.html', error_message=error_message)
        if not password:
            error_message = "You must provide a password!!!"
            return render_template('error_message.html', error_message=error_message)
        if not confirmation:
            error_message = "You must confirm your password!!!"
            return render_template('error_message.html', error_message=error_message)

        # Trimming white spaces in the information
        username = username.strip()
        password = password.strip()
        confirmation = confirmation.strip()

        if password != confirmation:
            error_message = "The confirmation does not match your password!!!"
            return render_template('error_message.html', error_message=error_message)

        db.execute("INSERT INTO users (username, pass) VALUES (?, ?)",
                        username, generate_password_hash(password))
        success_message = "Welcome! Your account was created successfully!"
        return render_template('success_message.html', success_message=success_message)


@app.route("/login", methods=["GET", "POST"])
@logout_required
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

    if not username:
            error_message = "You must provide a username!!!"
            return render_template('error_message.html', error_message=error_message)
    if not password:
            error_message = "You must provide a password!!!"
            return render_template('error_message.html', error_message=error_message)

    username = username.strip()
    password = password.strip()

    user_credentials = db.execute("SELECT id, pass FROM users WHERE username = ?", username)

    if not user_credentials :
            error_message = "Incorrect username!!!"
            return render_template('error_message.html', error_message=error_message)

    if not check_password_hash(user_credentials[0]["pass"], password):
            error_message = "Incorrect password!!!"
            return render_template('error_message.html', error_message=error_message)

    session["user_id"] = user_credentials[0]["id"]
    return redirect("/")


@app.route("/add-task", methods=["GET", "POST"])
@login_required
def add_task():
    if request.method == "GET":
        return render_template("add.html")
    if request.method == "POST":
        title = request.form.get("title")
        due_date = request.form.get("due_date")
        description = request.form.get("description")

        if not title:
            error_message = "You must provide a title!!!"
            return render_template('error_message.html', error_message=error_message)
        if len(title) > 50:
            error_message = "The max length of the title is 50!!!"
            return render_template('error_message.html', error_message=error_message)

        if description and len(description) > 100:
            error_message = "The max length of the title is 100!!!"
            return render_template('error_message.html', error_message=error_message)

        db.execute("INSERT INTO tasks (username_id, title, description, due_date) VALUES(?, ?, ?, ?)",
                    session["user_id"], title, description, due_date if due_date else None)
        success_message = "Great!, Task added successfully"
        return render_template('success_message.html', success_message=success_message, back=True)
    return ("/index")


@app.route("/get-tasks")
@login_required
def get_tasks():
    tasks = db.execute("SELECT title, starting_date AS start, due_date AS end, description from tasks WHERE username_id = ?",
                        session["user_id"])
    return jsonify(tasks)


@app.route("/delete-task", methods=["POST"])
@login_required
def delete_task():
    if request.method == "POST":
        task_id = request.form.get("task_id")
        if not task_id:
            error_message = "You must provide a task id!!!"
            return render_template('error_message.html', error_message=error_message)
        db.execute("DELETE FROM tasks WHERE id = ?", task_id)
    return redirect("/")


@app.route("/search", methods=["GET"])
@login_required
def search():
    return render_template("search.html")


@app.route("/search-task", methods=["GET"])
@login_required
def search_task():
    tasks = db.execute("SELECT id, title, description, strftime('%m-%d-%Y', starting_date) AS formatted_starting_date, strftime('%m-%d-%Y', due_date) AS formatted_due_date FROM tasks WHERE username_id = ? ORDER BY due_date NULLS LAST, starting_date;", session["user_id"])
    query = request.args.get("query")
    if query:
        tasks = db.execute("SELECT id, title, description, strftime('%m-%d-%Y', starting_date) AS formatted_starting_date, strftime('%m-%d-%Y', due_date) AS formatted_due_date FROM tasks WHERE username_id = ? AND title LIKE ?", session["user_id"], f"%{query}%")
        for task in tasks:
            due_date = task["formatted_due_date"]
            task["status"] = True
            if due_date:
                due_date_format = datetime.datetime.strptime(due_date, "%m-%d-%Y")
                current_date = datetime.datetime.now()
                task["status"] = True if ((due_date_format - current_date).days >= 0) else False
        return render_template("search_results.html", tasks=tasks)
    else:
        return redirect("/search")
