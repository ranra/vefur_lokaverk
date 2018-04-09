from app.config import Config
from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

if __name__ == '__main__':
      app.run()