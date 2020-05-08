import os
from flask import Blueprint, jsonify
from flask import render_template
from flask import g, session
from flask import request, make_response, redirect, url_for
from flask import current_app
from flask_cors import cross_origin
from functools import wraps
from app.config import get_admin_authorization_data
import app

admin = Blueprint("admin", __name__, template_folder="templates")

def admin_privilege_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_admin'):
            return redirect(url_for('admin.auth', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@admin.route('/auth', methods=['GET', 'POST'])
def auth():
    error = None
    if 'is_admin' in session:
        if session.get('is_admin'):
            return redirect(url_for('index'))
    if request.method == 'POST':
        login, password = get_admin_authorization_data()
        if request.form['login'] != login or request.form['password'] != password:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['is_admin'] = True
            return redirect(url_for('index'))
    return render_template('auth.html', error=error)


@admin.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'is_admin' in session:
        if session['is_admin']:
            session['is_admin'] = False
    return redirect(url_for('index'))


@admin.route("/editor")
@cross_origin()
@admin_privilege_required
def create_page():
    return render_template("editor.html", delete=False)

@admin.route("/editor/<path:path>")
@admin_privilege_required
def edit_page(path):
    page = app.pages.get_or_404(path)
    return render_template("editor.html", page=page, delete=True)

@admin.route('/save_article', methods=['POST'])
@admin_privilege_required
@cross_origin()
def save_article():
    filename = request.args.get('title') + '.md'
    with open(os.path.join(current_app.root_path, 'pages', filename), 'w', encoding="utf-8") as file:
        file.write(request.get_data().decode("utf-8"))
    return redirect(url_for('article', path=request.args.get('title')), code=301)

@admin.route('/delete_article', methods=['POST'])
@admin_privilege_required
@cross_origin()
def delete_article():
    filename = os.path.join(current_app.root_path, 'pages', request.args.get('title') + '.md')
    if os.path.exists(filename):
        os.remove(filename)
    return redirect(url_for('index'), code=301)
