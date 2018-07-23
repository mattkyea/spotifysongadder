#this comes from ACRCloud's examples (https://github.com/acrcloud/acrcloud_sdk_python/blob/master/mac/x86-64/python3/test.py)

import os, sys
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType

def identify():
    config = {
        'host':'identify-us-west-2.acrcloud.com',
        'access_key':'e0dec6b559cf1186da4b5283ab214b98',
        'access_secret':'k8Mb4sYf0A0xcVpptNb24m7uQ8jrGUSAR3nblN3X',
        'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO, # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The     SDK decide which type fingerprint to create accordings to "recognize_type".
        'debug':False,
        'timeout':10 # seconds
    }
    
    '''This module can recognize ACRCloud by most of audio/video file. 
        Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ...'''
    re = ACRCloudRecognizer(config)

    #recognize by file path, and skip 0 seconds from from the beginning of sound file.
    json = re.recognize_by_file("file.flac", 0, 10)
    #print(json)
    if "Success" not in json: #we have an error
        return "error recording song"
    else:
        #gonna cut out title and artist from what is returned
        start = json.index("\"artists\":[{\"name\":") + 20 ##20 chars before the stuff we want
        end = json.index("\"",start)
        artist = json[start:end]
        start = json.index("\"title\":\"") + 9
        end = json.index("\"",start)
        title = json[start:end]
        if "spotify" in json: #it has a spotify id
            start = json.index("spotify")
            json=json[start:]
            json = json[json.index("track"):]
            start = json.index("\"id\":\"") + 6
            end = json.index("\"",start)
            songId = json[start:end]
            print(title + " by " + artist)
            return songId
        else:#it does not have a spotify id
            return "Not on Spotify, but song is " + title + " by " + artist