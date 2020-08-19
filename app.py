from flask import (
    Flask,
    request,
)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2333,
    )
    app.run(**config)
