from flask import Flask,send_from_directory, render_template
import pyaudio
import wave
import time

app=Flask(__name__)



@app.route('/')
def  liveaudio():
    while True:
        filename = "recorded.wav"
        chunk = 1024
        FORMAT = pyaudio.paInt16
        channels = 1
        sample_rate = 44100
        record_seconds=0.3
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        output=True,
                        frames_per_buffer=chunk)
        frames = []
        for i in range(int(44100 / chunk * record_seconds)):
            data = stream.read(chunk)
            frames.append(data)
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(filename, "wb")
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames))
        wf.close()
        time.sleep(0.01)
        # return send_from_directory("/home/pi/Desktop/Final_Year_Project_Group12_PES/new_audio_codes", "recorded.wav")

@app.route('/home')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)