from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def config(app):
   db.init_app(app)
   app.db = db


class Contents(db.Model):
   __tablename__ = 'contents'

   id    = db.Column(db.String(36), primary_key=True, nullable=True)
   title = db.Column(db.String(256), nullable=True)
   body  = db.Column(db.Text)

   def __init__(self, id: str, title: str, body: int) -> None:
      self.id    = id
      self.title = title
      self.body  = body