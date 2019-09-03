from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    start_date = db.Column(db.TIMESTAMP,  nullable=False)
    end_date = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, comment, category_id):
        self.title = title
        self.start_date = start_date



class EventsSchema(ma.Schema):
    id = fields.Integer()
    title = fields.String(required=True)
    description = fields.String(required=True)
    creation_date = fields.DateTime()
    start_date = fields.DateTime()
    end_date = fields.DateTime()