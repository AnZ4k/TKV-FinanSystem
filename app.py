from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def bar() -> None:
    return render_template('login.html')


if __name__ == '__main__':
    app.run(port=60000)