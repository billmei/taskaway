from flask import render_template, send_from_directory
from flask import url_for, redirect, request
from . import app, db
from .forms import LoginForm
from config import EMAIL_CONFIRM_SALT

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
@app.route('/index')
def render_index_page():
    return render_template('index.html')
@app.route('/signup', methods=["GET", "POST"])
def render_signup_page():
    form = LoginForm()

    if form.validate_on_submit():
        user = User(
            email = form.email.data,
            _password = form.password.data
        )
        db.session.add(user)
        db.session.commit()

        login_user(user)

        return redirect(url_for('dashboard'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def render_login_page():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first_or_404()
        if user.is_correct_password(form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('index'))

    return render_template('login.html', form=form)

@app.route('/signout')
def signout():
    logout_user()
    return redirect(url_for('index'))
    
@app.route('/dashboard')
def render_dashboard_page():
    return render_template('dashboard.html')
    @app.route('/confirm/<token>')
    def confirm_email(token):
        try:
            email = ts.loads(token, salt=EMAIL_CONFIRM_SALT, max_age=86400)
        except:
            abort(404)

        user = User.query.filter_by(email=email).first_or_404()

        user.email_confirmed = True

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('signin'))

# Error Handlers
@app.errorhandler(400)
def render_error(error):
    return render_template('error.html', errorcode=400), 400
@app.errorhandler(401)
def render_error(error):
    return render_template('error.html', errorcode=401), 401
@app.errorhandler(403)
def render_error(error):
    return render_template('error.html', errorcode=403), 403
@app.errorhandler(404)
def render_error(error):
    return render_template('error.html', errorcode=404), 404
@app.errorhandler(500)
def render_error(error):
    return render_template('error.html', errorcode=500), 500
