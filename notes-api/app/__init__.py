
from flask import Flask
from .config import Config
from .models import db
from .routes import bp as notes_bp

def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(notes_bp, url_prefix="/")

    @app.route("/health")
    def health():
        return {"status": "ok"}, 200

    return app
