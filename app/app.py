from flask import Flask, render_template, request

from app.database import init_db

import models

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    init_db(app)

    return app

app = create_app()

@app.route('/')
@app.route('/home')
def wellcom():
    return render_template("home/index.html")

@app.route('/report')
def index():
    return render_template("daily_report/index.html")

@app.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        date = request.form.get('date')
        title = request.form.get('title')
        content = request.form.get('content')

        db.session.add(app)

    return render_template("daily_report/create.html")

if __name__ == "__main__":
    app.run(debug=True)