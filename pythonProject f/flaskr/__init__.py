#インポートされる時に実行されるもの
#初期化処理

from flask import Flask

def create_app():
  app = Flask(__name__)

  with app.app_context():
    from . import main
    from . import db
    db.create_books_table()
  
  return app