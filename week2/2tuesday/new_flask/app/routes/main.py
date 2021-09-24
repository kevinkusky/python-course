from flask import Blueprint, render_template, redirect


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


@bp.route('/help')
def help():
    return render_template('page.html', title='Help')

