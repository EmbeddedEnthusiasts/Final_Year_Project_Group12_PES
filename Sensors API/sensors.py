from flask import Flask
import json
from random import seed, randint

seed(1)


app = Flask(_name_)

@app.route('/')
def get():
    data={
        "left":randint(0,10),
        "right":randint(0,10),
        "back":randint(0,10),
    }
    data_json=json.dumps(data)
    return data_json


if _name=="main_":
    app.run(debug=True)