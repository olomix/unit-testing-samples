from collections import namedtuple

import sqlite3
from time import sleep

from flask import Flask, render_template_string, g

app = Flask(__name__)
app.config["DB"] = "/Users/alek/Documents/src/testing-222/webapp/db.sqlite"

User = namedtuple("User", ("id", "name"))
Ad = namedtuple("Ad", ("title", "url"))

## BD

def get_db():
    if not hasattr(g, "db"):
        g.db = sqlite3.connect(app.config["DB"])
    return g.db


def ads():
    sleep(0.5)
    return [
        Ad("bike", "http://google.com"),
    ]


## BL

def list_all_users():
    return [
        User(user[0], user[1])
        for user in
        get_db().execute("select id, name from user order by id").fetchall()
    ]

@app.route("/")
def index():
    return render_template_string(
        """
        <table>
        {% for user in users %}
        <tr><td>{{user.id}}</td><td>{{user.name}}</td></tr>
        {% endfor %}
        </table>
        {% for ad in ads %}
        <p><a href="{{ad.url}}">{{ad.title}}</a></p>
        {% endfor %}
        """,
        users=list_all_users(),
        ads=ads(),
    )

if __name__ == '__main__':
    app.run()