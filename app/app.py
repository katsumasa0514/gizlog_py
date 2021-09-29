from flask import Flask, render_template, request, redirect, url_for

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

@app.route('/report/<int:id>')
def show(id):
    daily_reports = DailyReport.query.filter(DailyReport.id == id).first()

    return render_template("daily_report/show.html", daily_reports=daily_reports)

@app.route('/report/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        date = request.form.get('date')
        title = request.form.get('title')
        content = request.form.get('content')
        daily_report = DailyReport(date, title, content)

        db.session.add(daily_report)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template("daily_report/create.html")

@app.route('/report/<int:id>/edit', methods=["GET", "POST"])
def edit(id):
    daily_reports = db.session.query(DailyReport).filter_by(id=id).first()
    """ print(daily_reports, flush=True) """

    if request.method == "POST":
        daily_reports.reporting_time = request.form.get('date')
        daily_reports.title = request.form.get('title')
        daily_reports.content = request.form.get('content')

        db.session.add(daily_reports)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template("daily_report/edit.html", daily_reports=daily_reports)


if __name__ == "__main__":
    app.run(debug=True)