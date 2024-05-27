from app import db
import uuid

class QRCode(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    url = db.Column(db.String(200), nullable=False)
    dynamic = db.Column(db.Boolean, default=False)
    scans = db.Column(db.Integer, default=0)
