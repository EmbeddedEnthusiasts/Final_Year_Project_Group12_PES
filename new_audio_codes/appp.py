from flask import Flask,send_from_directory,render_template
import pyaudio
import wave


appp=Flask(__name__)

def  liveaudio():
    filename = "recorded.wav"
    chunk = 1024
    FORMAT = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    record_seconds=0.5
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                channels=channels,
                rate=sample_rate,
                input=True,
                output=True,
                frames_per_buffer=chunk)
    frames = []
    for i in range(int(sample_rate/chunk*record_seconds)):
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
    return render_template("index.html")
    

@appp.route('/')
def index():
    while True:
        liveaudio()

if __name__=="__main__":
    appp.run(debug=True)