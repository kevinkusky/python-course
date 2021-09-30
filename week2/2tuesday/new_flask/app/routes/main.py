from flask import Blueprint, render_template, redirect, session
from app.forms.login import LoginForm

bp = Blueprint('', __name__)


def track_views():
    if 'views' in session:
        # session is dict
        session['views'] = session.get('views') + 1
    else:
        session['views'] = 1


@bp.route('/')
def index():
    # Basic Return
    # return '<h1>Sample App</h1>'
    # Multi-Line Return
    # return """<h1>I am a header</h1>
    #         <p>I am a paragraph</p>
    #         <a href='/help'>Need Help?</a>
    #         """
    # Template Return
    # render_template('template_title.html', var_name='var_value')
    track_views()
    return render_template('page.html', title='Index')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', form=form)


@bp.route('/views')
def views():
    return f'Total Views: {session.get("views")}'


@bp.route('/views/reset')
def reset_views():
    views = session.pop('views', None)
    return f'Reset Views!  Previous View Count: {views}'


@bp.route('/help')
def help():
    track_views()
    return render_template('page.html', title='Help')

