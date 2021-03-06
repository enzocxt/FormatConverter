import json

from flask import (
    Flask,
    request,
    jsonify,
)

from models.conversion import Conversion
from utils import (
    json2csv,
    csv2json,
    csv2yaml,
    yaml2csv,
    json2yaml,
    yaml2json,
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
    fmt_from = org_data.get('from', 'json')
    fmt_to = org_data.get('to', 'csv')

    func_map = {
        ('json', 'csv'): json2csv,
        ('csv', 'json'): csv2json,
        ('csv', 'yaml'): csv2yaml,
        ('yaml', 'csv'): yaml2csv,
        ('json', 'yaml'): json2yaml,
        ('yaml', 'json'): yaml2json,
    }
    data = org_data.get('data', '')
    converter = func_map.get((fmt_from, fmt_to), None)
    res = converter(data)

    form = {
        'from': fmt_from,
        'to': fmt_to,
        'input_data': data,
        'output_data': res,
    }
    conversion = Conversion(form)
    conversion.save()
    return res


@app.route('/converts', methods=['GET'])
def get_converts():
    conversions = Conversion.all()
    conversions = [conv.json() for conv in conversions]
    res = jsonify(conversions)
    return res


@app.route('/converts/<int:id>', methods=['GET'])
def get_convert(id):
    conversion = Conversion.find(id)
    conversion = conversion.json()
    res = jsonify(conversion)
    return res


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2333,
    )
    app.run(**config)
