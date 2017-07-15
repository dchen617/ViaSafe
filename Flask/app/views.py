from app import app
from flask import render_template, jsonify


@app.route("/")
def main():
    return render_template('index.html')
