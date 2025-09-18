from app.extensions import db
from datetime import datetime

class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class StatusLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'), nullable=False)
    status_code = db.Column(db.Integer)
    checked_at = db.Column(db.DateTime, default=datetime.utcnow)

    site = db.relationship('Site', backref=db.backref('logs', lazy=True))
