from flask import Flask
from flask_cors import CORS
from extensions import db, jwt
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)
    jwt.init_app(app)

    from routes import auth, view

    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(view, url_prefix="/")
    

    with app.app_context():
        db.create_all()


    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
