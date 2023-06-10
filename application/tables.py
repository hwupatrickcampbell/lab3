from application import app
from flask_sqlalchemy import SQLAlchemy
from application import config

db = SQLAlchemy(app)

class Ticket(db.Model):
    __tablename__ = 'tickets'
    TicketNumber = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    TYPE = db.Column(db.String(100), nullable=False)
    StoryPoints = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Ticket %r>' % self.Ticket

