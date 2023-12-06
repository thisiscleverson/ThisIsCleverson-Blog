import os
from flask import Flask
from flask_migrate import Migrate

from .models import config as config_db


def create_app():
   app = Flask(__name__)
   #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   app.config['SERVER_NAME'] = 'localhost:5000'
   
   config_db(app)
   
   Migrate(app, app.db)

   from .blog import bp_blog
   app.register_blueprint(bp_blog)
   return app 