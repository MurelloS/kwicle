from math import ceil
from flask import Flask, render_template, request
from flask_flatpages import FlatPages
from app.config import configure_app
from app.admin import admin

app = Flask(
    __name__,
    static_url_path="/static/dist",
    static_folder="static/dist",
    instance_relative_config=True
)
configure_app(app)




app.register_blueprint(admin, url_prefix="/admin")

pages = FlatPages(app)

from app import views