from flask import Blueprint, render_template, redirect
from app.forms.login import LoginForm

bp = Blueprint('', __name__)

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
    return render_template('page.html', title='Index')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', form=form)


@bp.route('/help')
def help():
    return render_template('page.html', title='Help')

