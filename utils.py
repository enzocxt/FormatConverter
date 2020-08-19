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
