from flask import (Flask, url_for, request,
            render_template, make_response,
            session, escape, redirect)

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
    # return 'Hello world!'
    context = {'name': name}
    return render_template('hello.html', **context)

@app.route('/')
def index():
    if 'session_id' in session and 'test_value' in session:
        return 'Logged in as {}, test value = {}'.\
                format(escape(session['session_id']), 
                    escape(session['test_value']))
    return 'You are not logged in'

@app.route('/post/<int:post_id>')
def show_post_id(post_id):
    return 'Post id = {}'.format(str(post_id))

@app.route('/path/<path:path_value>')
def show_path_value(path_value):
    return 'Path : {}'.format(path_value)

@app.route('/test')
def show_result():
    result = []
    result.append(url_for('hello_world'))
    result.append(url_for('show_post_id', post_id = 5566))
    result.append(url_for('show_path_value', path_value='so_strange_haha/1.0.2'))
    result.append(url_for('static', filename='style.css'))
    return '<br/>'.join(result)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['session_id'] = request.form['username'] 
        session['test_value'] = request.form['test_value']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=text name=test_value>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/set_cookie')
def set_cookie():
    resp = make_response(render_template('hello.html', name='cookie'))
    resp.set_cookie('username', 'moonblack')
    return resp

@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username', 'no_value')
    return username
