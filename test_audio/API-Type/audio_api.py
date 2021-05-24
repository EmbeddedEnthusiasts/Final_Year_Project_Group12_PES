from flask import Flask
import pyaudio
import json

streamer=Flask(_name_)

FORMAT=pyaudio.paInt16
CHANNELS=2
RATE=44100
CHUNK=1024

aud=pyaudio.PyAudio()

@streamer.route('/aud')
def getaud():
    global aud
    stream=aud.open(format=FORMAT, channels=CHANNELS,rate=RATE, input=True,input_device_index=2,frames_per_buffer=CHUNK)
    data=stream.read(CHUNK, exception_on_overflow = False)
    data_mp3=(b'--frame\r\n'
                   b'Content-Type: audio/mp3\r\n\r\n' + data + b'\r\n')
    data_dict={
        'audio':data_mp3,
    }
    data_json=json.dumps(data_dict)
    return data_json


if _name=="main_":
    streamer.run(debug=True)