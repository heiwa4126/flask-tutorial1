#!/usr/bin/env python
# -*- coding: utf-8 -*
"""
Flask example
"""
from flask import Flask
from flask import render_template
from flask import make_response
from flask import request


app = Flask(__name__)


@app.route("/")
def index():
    """画面表示
    Returns:
        render_template: index.html
    """
    return render_template("index.html")


@app.route("/hello", methods=["POST"])
def hello():
    """文字列表示
    Returns:
        make_response: 表示文字列
    """
    name = request.form.get("name")
    return make_response("こんにちは、" + name + "さん")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
