# spotifysongadder
records, identifies, and adds whatever your're listening to into a spotify playlist

### recorder.py
records 10 seconds of audio using PyAudio ()

### identify.py
uses ACRCloud's service to identify the recorded audio, returning a title, artist, and Spotify ID if found

### spotify.py
ties it all together using Spotipy () 

# bugs
need to clean up print statements and everything in general
occasional error with identifying if on quiet part of song
occasional error with adding (incorrect id with september for ex?)
maybe put on a website 
