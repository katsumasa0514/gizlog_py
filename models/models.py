from datetime import datetime
from app.database import db


class DailyReport(db.Model):

    __tablename__ = 'daily_reports'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    reporting_time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    deleted_at = db.Column(db.DateTime, nullable=True, onupdate=datetime.now)
