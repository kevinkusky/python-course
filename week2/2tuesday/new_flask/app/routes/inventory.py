from flask import Blueprint, render_template


bp = Blueprint('inventory', __name__, url_prefix='/inventory')


@bp.route('/item/<int:id>')
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