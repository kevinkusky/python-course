from app import app


@app.route('/')
def index():
    # return '<h1>Sample App</h1>'
    return """<h1>I am a header</h1>
            <p>I am a paragraph</p>
            <a href='/help'>Need Help?</a>
            """


@app.route('/help')
def help():
    return """<h1>Do Yo Need Help?</h1>
                <p>We all need help! Go back <a href='/'>Home</a></p>
            """


@app.route('/item/<int:id>')
def item(id):
    if (id > 0 and id < 100):
        return f'<h1>Sampe App</h1><p>Item {id}</p>'
    else:
        return f'<h1>Sampe App</h1><p>Item {id} not found</p>'
    
