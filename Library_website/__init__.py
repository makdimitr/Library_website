from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import sqlalchemy as sa

db = SQLAlchemy() 
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'blablabla' # secure the cookies/session data related to website
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
 
    from .models import User, Book  

    with app.app_context():
        db.create_all()
        
        """     Attempt to remove the unique constraint from the books
        with db.engine.connect() as conn:
            books_table = db.Table('books_table', db.metadata, autoload=True, autoload_with=conn)
            unique_constraint = [c for c in books_table.constraints if isinstance(c, sa.UniqueConstraint) and books_table.columns['id'] in c.columns]
            if unique_constraint:
                conn.execute(sa.schema.DropConstraint(unique_constraint[0]))
        """
    

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')