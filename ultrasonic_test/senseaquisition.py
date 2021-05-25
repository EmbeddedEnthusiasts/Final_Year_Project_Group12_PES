from flask import *
import hcsr

left=hcsr.Ultrasonic(16,18)

app = Flask(__name__)

@app.route('/')
def get():
    return jsonify(
        l = left.getDistance()
    )

@app.route('/home')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="192.168.0.20", debug=True)

