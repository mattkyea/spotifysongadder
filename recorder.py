import pyaudio
import sys
import wave
from array import array 

def record():
    
    chunk = 2048
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "file.flac"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS, 
                    rate=RATE, 
                    input=True,
                    output=True,
                    frames_per_buffer=chunk,
                    input_device_index = 0)
    
    print("* recording")

    frames = []

    for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
            data = stream.read(chunk)
            data_chunk=array('h',data)
            vol=max(data_chunk)
            # check for silence here by comparing the level with 0 (or some threshold) for the contents of data.
            if(vol>=500): 
                # then write data or not to a file
                frames.append(data) 
    
    print("* done")

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("write the file")

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(p.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close() 