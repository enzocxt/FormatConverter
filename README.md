# FormatConverter
This test project makes use of the Python Flask framework.  
Run the server by command `$ python app.py` which makes the server run on `http://localhost:2333`.  
The database is not implemented with popular databases. While I directly save and read data through files (`data/Conversion.txt`). It helps me to implement the model classes quickly. And the current model classes would be easily transferred to other databases.

## Test APIs
Instructions of how to test by Linux CLI tools (curl command line).  

### Converter API
`/convert`
```
# test conversion from 'json' to 'csv'
$ curl -s -H "Content-Type:application/json" -X POST -d '{"from": "json", "to": "csv", "data": "[{\"name\": \"John\", \"surname\": \"Doe\"}, {\"name\": \"Jane\", \"surname\": \"Doe\"}]"}' http://127.0.0.1:2333/convert

# test conversion from 'csv' to 'json'
$ curl -s -H "Content-Type:application/json" -X POST -d '{"from": "csv", "to": "json", "data": "name,surname\r\nJohn,Doe\r\nJane,Doe\r\n"}' http://127.0.0.1:2333/convert

# test conversion from 'csv' to 'yaml'
$ curl -s -H "Content-Type:application/json" -X POST -d '{"from": "csv", "to": "yaml", "data": "name,surname\r\nJohn,Doe\r\nJane,Doe\r\n"}' http://127.0.0.1:2333/convert

# test conversion from 'yaml' to 'csv'
$ curl -s -H "Content-Type:application/json" -X POST -d '{"from": "yaml", "to": "csv", "data": "- name: John\n  surname: Doe\n- name: Jane\n  surname: Doe\n"}' http://127.0.0.1:2333/convert

# test conversion from 'json' to 'yaml'
$ curl -s -H "Content-Type:application/json" -X POST -d '{"from": "json", "to": "yaml", "data": "[{\"name\": \"John\", \"surname\": \"Doe\"}, {\"name\": \"Jane\", \"surname\": \"Doe\"}]"}' http://127.0.0.1:2333/convert

# test conversion from 'yaml' to 'json'
$ curl -s -H "Content-Type:application/json" -X POST -d '{"from": "yaml", "to": "json", "data": "- name: John\n  surname: Doe\n- name: Jane\n  surname: Doe\n"}' http://127.0.0.1:2333/convert
```

### History Of Conversion
`/converts`
```
$ curl -s http://127.0.0.1:2333/converts
```

`/converts/1`
```
$ curl -s http://127.0.0.1:2333/converts/1
```
