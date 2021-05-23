from flask import Flask
import json
from random import seed, randint
import hcsr

left=hcsr.Ultrasonic(16,18)

seed(1)


app = Flask(__name__)

@app.route('/')
def get():
    data={
        "left": left.getDistance(),
        # "right":randint(0,10),
        # "back":randint(0,10),
    }
    data_json=json.dumps(data)
    return data_json


if __name__=="__main__":
    app.run(debug=True)

