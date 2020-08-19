import io
import json
import csv
import yaml
import pandas as pd


def json2csv(json_string):
    dict_data = json.loads(json_string)
    df = pd.DataFrame(dict_data)
    csv_string = df.to_csv(index=False)
    return csv_string


def csv2json(csv_string):
    reader = csv.DictReader(io.StringIO(csv_string))
    json_data = json.dumps([row for row in reader])
    return json_data


def json2yaml(json_string):
    data = json.loads(json_string)
    yaml_data = yaml.dump(data)
    return yaml_data


def yaml2json(yaml_string):
    buffer = io.StringIO(yaml_string)
    data = yaml.safe_load(buffer)
    json_data = json.dumps(data)
    return json_data


def csv2yaml(csv_string):
    reader = csv.DictReader(io.StringIO(csv_string))
    yaml_data = yaml.dump([dict(row) for row in reader])
    return yaml_data


def yaml2csv(yaml_string):
    buffer = io.StringIO(yaml_string)
    data = yaml.safe_load(buffer)
    df = pd.DataFrame(data)
    csv_string = df.to_csv(index=False)
    return csv_string


json_list = [
    '[{"name": "John", "surname": "Doe"}, {"name": "Jane", "surname": "Doe"}]'
]
csv_list = [
    'name,surname\r\nJohn,Doe\r\nJane,Doe\r\n'
]
yaml_list = [
    '- name: John\n  surname: Doe\n- name: Jane\n  surname: Doe\n'
]


def test_json2csv():
    for data, res in zip(json_list, csv_list):
        assert json2csv(data) == res


def test_csv2json():
    for data, res in zip(csv_list, json_list):
        assert csv2json(data) == res


def test_json2yaml():
    for data, res in zip(json_list, yaml_list):
        assert json2yaml(data) == res


def test_yaml2json():
    for data, res in zip(yaml_list, json_list):
        assert yaml2json(data) == res


def test_csv2yaml():
    for data, res in zip(csv_list, yaml_list):
        assert csv2yaml(data) == res


def test_yaml2csv():
    for data, res in zip(yaml_list, csv_list):
        assert yaml2csv(data) == res
