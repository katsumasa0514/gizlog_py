from flask import Flask, render_template, request

from app.database import init_db, db

from models.models import DailyReport

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
    daily_reports = DailyReport.query.all()

    return render_template("daily_report/index.html", daily_reports=daily_reports)

@app.route('/<int:id>')
def show(id):
    daily_reports = DailyReport.query.filter(DailyReport.id == id).all()
    """ print(daily_reports, flush=True) """

    return render_template("daily_report/show.html", daily_reports=daily_reports)

@app.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        date = request.form.get('date')
        title = request.form.get('title')
        content = request.form.get('content')
        daily_report = DailyReport(date, title, content)

        db.session.add(daily_report)
        db.session.commit()

    return render_template("daily_report/create.html")

if __name__ == "__main__":
    app.run(debug=True)