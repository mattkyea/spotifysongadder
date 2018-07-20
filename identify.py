#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
    >>> python test.py test.mp3
'''

import os, sys
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType

def identify():
    config = {
        'host':'identify-us-west-2.acrcloud.com',
        'access_key':'e00fce65717e122400eab1f48bc3a56b',
        'access_secret':'q2ut3sFlk3VwUIE9NYE71gpj3gvfmo5eiaibSFx8',
        'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO, # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The     SDK decide which type fingerprint to create accordings to "recognize_type".
        'debug':False,
        'timeout':10 # seconds
    }
    
    '''This module can recognize ACRCloud by most of audio/video file. 
        Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ...'''
    re = ACRCloudRecognizer(config)

    #recognize by file path, and skip 0 seconds from from the beginning of sys.argv[1].
    json = re.recognize_by_file("file.flac", 0, 10)
    #print(json)
    if "No result" in json:
        print("error recording song")
        return "error recording song"
    else:
        start = json.index("\"artists\":[{\"name\":") + 20 ##20 chars before the stuff we want
        end = json.index("\"",start)
        artist = json[start:end]
        start = json.index("\"title\":\"") + 9
        end = json.index("\"",start)
        title = json[start:end]
        start = json.index("spotify")
        if start != 1:
            json=json[start:]
            json = json[json.index("track"):]
            start = json.index("\"id\":\"") + 6
            end = json.index("\"",start)
            songId = json[start:end]
            ##return songId
            print(songId + ", "+ title + " by " + artist)
            return songId
        else:
            ##return "Not on Spotify, but song is " + title + " by " + artist
            print("Not on Spotify, but song is " + title + " by " + artist)
            return "Not on Spotify, but song is " + title + " by " + artist