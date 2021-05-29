from flask import *
import hcsr
import cv2

app = Flask(__name__)
#pin=hcsr.Ultrasonic(T,E)
left=hcsr.Ultrasonic(19,21)
right=hcsr.Ultrasonic(22,23)
back=hcsr.Ultrasonic(24,26)


camera = cv2.VideoCapture(0)  # use 0 for web camera
#  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera

def gen_frames():
    global camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/sensors-api')
def getSensorValue():
    return jsonify(
        l = left.getDistance(),
        r = right.getDistance(),
        # b = back.getDistance()
    )

@app.route('/home')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
