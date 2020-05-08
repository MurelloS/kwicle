from flask import render_template, request
from math import ceil
from app import app
from app import pages


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route('/')
@app.route('/index')
def index():
    page_number = request.args.get("page", default=1, type=int)

    _articles = [p for p in pages if 'published' in p.meta]
    latest = sorted(_articles, reverse=True,
                    key=lambda p: p.meta['published'])
    max_page = ceil(len(_articles) / 9)
    return render_template('index.html', articles=latest[(page_number-1)*9:(page_number)*9], page_number=page_number, max_page=max_page)


@app.route('/catalog')
def catalog():
    articles = (p for p in pages if 'published' in p.meta)
    _catalog = dict()
    unsorted = []
    for page in articles:
        if ('subject' in page.meta):
            if (page.meta["subject"] == "Несортированное"):
                unsorted.append(page)
            else:
                _catalog.setdefault(page.meta['subject'], []).append(page)
    return render_template('catalog.html', catalog=_catalog, unsorted= unsorted)


@app.route("/unpublished_articles")
def unpublished_articles():
    articles = (p for p in pages if 'published' not in p.meta)
    _catalog = dict()
    unsorted = []
    for page in articles:
        if ('subject' in page.meta):
            if (page.meta["subject"] == "Несортированное"):
                unsorted.append(page)
            else:
                _catalog.setdefault(page.meta['subject'], []).append(page)
    return render_template('catalog.html', catalog=_catalog, unsorted= unsorted)


@app.route("/<path:path>/")
def article(path):
    page = pages.get_or_404(path)
    return render_template("article.html", page=page)


@app.route("/tutor/<path:path>/")
def tutor(path):
    page = pages.get_or_404(path)
    return render_template("article.html", page=page)

@app.route("/.well-known/acme-challenge/TGy9o84drNjLkUxgmFLnyOw8g56756uPUCW0gJJSZig")
def ssl():
    return "TGy9o84drNjLkUxgmFLnyOw8g56756uPUCW0gJJSZig.2hWwTKTUhLGH7g6SzX2r8c6aJRZcKVHoHOhurCR00aU"


