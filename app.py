import json

from flask import (
    Flask,
    request,
)

from utils import (
    json2csv,
    csv2json,
)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/convert', methods=['POST'])
def convert():
    """
    data: {"from": "json", "to": "csv", "data": "[{"name": "John", "surname": "Doe"}, {"name": "Jane", "surname": "Doe"}]"}
    """
    data = request.data
    data_string = data.decode('utf-8')
    org_data = json.loads(data_string)
    print('Original data:\n', org_data)
    fmt_from = org_data.get('from', 'json')
    fmt_to = org_data.get('to', 'csv')
    func_map = {
        ('json', 'csv'): json2csv,
        ('csv', 'json'): csv2json,
    }
    data = org_data.get('data', '')
    print(f'data[{type(data)}]:\n', data)
    converter = func_map.get((fmt_from, fmt_to), None)
    res = converter(data)
    return res


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2333,
    )
    app.run(**config)
