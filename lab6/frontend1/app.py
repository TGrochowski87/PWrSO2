from flask import Flask
from flask import request, redirect, url_for

import database_manager as dm

app = Flask(__name__)

@app.route("/")
def home():
    return """
        <body style="background-color:lightgrey;">
        <h1>List of urls</h1>
        <ul>
        <li>/list - TODO list</li>
        <li>/add - add new task to list</li>
        </ul>
        </body>
    """


@app.route("/list/", methods = ["POST", "GET"])
def list():

    tasks_unchecked = dm.get_tasks_unchecked()
    tasks_checked = dm.get_tasks_checked()

    if request.method == "GET":
        html = f"<body style='background-color:lightgrey;'><form method='POST'><h1>TODO</h1><ul>"
        for x in tasks_unchecked:
            html += f"<li>{str(x['text'])}</li>"
        html += "</ul><h1>DONE</h1><ul>"
        for x in tasks_checked:
            html += f"<li>{str(x['text'])}</li>"
        html += f"</ul>"
        html += f"<label for='chosen'>Task for status changing</label> <input name='task' id='chosen' /> <button type='submit'>Confirm change</button></form></body>"
        return html

    if request.method == "POST":
        dm.change_task_status(request.form.get("task"))

        return redirect(url_for("list"))


@app.route("/add/", methods = ["POST", "GET"])
def add():
    if request.method == "GET":
        return """
        <body style="background-color:lightgrey;">
        <form method="POST">
            <input name="task"/>
            <button type="submit">Dodaj zadanie</button>
        </form></body>
        """

    if request.method == "POST":
        dm.add_task(request.form.get("task"))

        return redirect(url_for("add"))