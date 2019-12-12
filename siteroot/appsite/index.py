# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, redirect, flash, abort
from flask_login import login_user, login_required, logout_user, current_user

from appsite import app
#from watchlist.models import User, Movie

@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('404.html'), 404  # 返回模板和状态码

@app.route("/hello")
def hello():
    return "<h1>hello, world</h1>"

@app.route("/")
def index():
    return render_template('base.html')

@app.route('/404')
def a404():
    abort(404)

