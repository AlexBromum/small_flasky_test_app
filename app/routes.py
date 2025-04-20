# -*- coding: utf-8 -*-

from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Гость"}
    posts = [
        {
            "data_time": "Сегодня",
            "body": "А сегодня произошло вот это",
        },
        {"data_time": "Вчера", "body": "А вчера было вон то!"},
        {"data_time": "7 07 2707", "body": "JKf8389/"},
    ]
    return render_template("index.html", title="Главная", user=user, posts=posts)
