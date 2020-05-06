"""Flask config class."""
import os
import mistune
from flask import render_template_string

MD_EXTENSION = ['admonition', "toc", "nl2br", "codehilite", "fenced_code", "tables"]
def my_markdown(text):
    markdown_text = render_template_string(text)
    # pygmented_text = markdown.markdown(markdown_text, extensions=MD_EXTENSION)
    return mistune.html(markdown_text)

class Config:
    """Base config vars."""
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    FLATPAGES_AUTO_RELOAD = 1
    FLATPAGES_EXTENSION = [".md", ".markdown"]
    FLATPAGES_HTML_RENDERER = my_markdown
    # FLATPAGES_ROOT = 'articles/pages'
    # SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')


class ProductionConfig(Config):
    """Prod. config vars."""
    SECRET_KEY = "fc7c70d3afaedc23fe91f9fe3f452972"
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Dev. config vars."""
    SECRET_KEY = "fc7c70d3afaedc23fe91f9fe3f452972"
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    """Test. config vars."""
    SECRET_KEY = "fc7c70d3afaedc23fe91f9fe3f452972"
    DEBUG = True
    TESTING = True

CONFIG = {
    "development": "app.config.DevelopmentConfig",
    "testing": "app.config.TestingConfig",
    "production": "app.config.ProductionConfig",
    "default": "app.config.DevelopmentConfig",
}

def configure_app(app):
    """
    Configure app from env variable
    """
    config_name = os.getenv('FLASK_ENV', 'default')
    app.config.from_object(CONFIG[config_name])

def get_admin_authorization_data():
    login = "PALATA111"
    password = "111KAMARDINWASAMISTAKE111"
    return login, password
    