#runs the web_static file

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
