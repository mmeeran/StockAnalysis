from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

#simple route
@views.route("/")
def home():
    return render_template("index.html", name="Mo")

#Accessing Request object
@views.route("/profile")
def profile():
    args = request.args
    uName = args.get('name')
    return render_template("index.html", name=uName)

#Send Jason object 
@views.route("/json")
def get_json():
    return jsonify({'name':'Mohamed Meeran', 'age':52})

@views.route("/redir")
def redir():
    return render_template("redirected.html")

#redirect to a page
@views.route("/redirectpg")
def redirectpg():
    return redirect(url_for("views.redir"))