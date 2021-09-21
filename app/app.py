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
def hello_world():
    return render_template("home/index.html")

if __name__ == "__main__":
    app.run(debug=True)

""" @app.route('/report')
def hello_world():
    return render_template("home/index.html") """