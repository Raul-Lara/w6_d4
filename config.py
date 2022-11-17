import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

# Gvie acces to the project form any operating System
#We find ourselfs in
#Allow outside files/folders to be added to the project from the
#Base firectory

load_dotenv(os.path.join(basedir, '.env'))

class Config():
  """
  Set config variables for the flask app.
  Using enviroment variables where available
  Otherwise create tje config variable if not done already.
  """

  SECRET_KEY = os.environ.get('SECRET_KEY') or 'Nana nana boo boo youll never guess!'
  FLASK_APP = os.environ.get('FLASK_APP')
  FLASK_ENV = os.environ.get('FLASK_ENV')
  SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

  SQLALCHEMY_TRACK_MODIFICATIONS = False #turns off updates from sqlalchemy