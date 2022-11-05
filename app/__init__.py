from flask import Flask

def create_app():
    app = Flask(__name__)
    #from app.models import db
    #db.init_app(app)

    from app.views.demo_view import DemoViews

    demo_views = DemoViews().demo_page_views
    app.register_blueprint(demo_views, url_prefix="/")

    return app
