from flask import render_template, send_from_directory
from flask import url_for, redirect, request
from app import app

# Deletes trailing slashes before loading the page
@app.before_request 
def remove_trailing_slash(): 
    if request.path != '/' and request.path.endswith('/'): 
        return redirect(request.path[:-1], code=301) 

# Redirects to the template renderer to strip .html extension
@app.route('/<pagename>.html')
def render_html_page(pagename):
    return redirect(url_for('render_' + pagename + '_page'), code=301)

# (Pseudo) static html pages
@app.route('/')
def render_index_page():
    return render_template('index.html')

# Error Handlers
@app.errorhandler(400)
def page_not_found(error):
    return render_template('error.html', errorcode=400), 400
@app.errorhandler(401)
def page_not_found(error):
    return render_template('error.html', errorcode=401), 401
@app.errorhandler(403)
def page_not_found(error):
    return render_template('error.html', errorcode=403), 403
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', errorcode=404), 404
@app.errorhandler(500)
def server_error(error):
    return render_template('error.html', errorcode=500), 500
