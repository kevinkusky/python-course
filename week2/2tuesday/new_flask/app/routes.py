from flask import render_template
from app import app


@app.route('/')
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


@app.route('/help')
def help():
    return render_template('page.html', title='Help')


@app.route('/item/<int:id>')
def item(id):
    # if (id > 0 and id < 100):
    #     return f'<h1>Sampe App</h1><p>Item {id}</p>'
    # else:
    #     return f'<h1>Sampe App</h1><p>Item {id} not found</p>'
    item = {
        'id': id,
        'name': f'Item Name for ID: {id}',
        'description': 'coming soon!'
    }
    return render_template('item.html', item=item)

