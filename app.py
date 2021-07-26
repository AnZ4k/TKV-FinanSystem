from flask import Flask, request, render_template, sessions, url_for, redirect, url_for

app = Flask(__name__)
session = {}

@app.route('/')
def bar() -> None:
    if not 'session' in session:
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/login')
def login() -> None:
    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=60000)