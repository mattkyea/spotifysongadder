# spotifysongadder
records, identifies, and adds whatever your're listening to into a spotify playlist called "Songs Added from Song Finder"

how it works:

-run "python spotify.py username" with username being your spotify username

-paste the link that pops up in your browser back into the console (this happens twice, and is Spotify's 
authentication - allowing me to read, create, and add to your playlists)

-I check for a playlist titled "Songs Added from Song Finder" in your playlists, creating it if it doesn't exist, then getting its id for later use

-recorder.py is called, recording whatever is playing on your computer (works best with headphone mic)

-identify.py is called with that recording, returning either the song's id, title with artist, or an error

-the id is used to see if the song is already in the playlist (no repeats)

-if the song isn't in the playlist, its added

-the process starts over at recording

### recorder.py
records 10 seconds of audio using PyAudio (http://people.csail.mit.edu/hubert/pyaudio/), saving the file as file.flac (possibly higher quality than mp3). This sample will be used to identify the song.

### identify.py
uses ACRCloud's service (https://www.acrcloud.com/docs/acrcloud/tutorials/identify-music-by-sound/) to identify the recorded audio, returning a title, artist, and Spotify ID if found. Works like Shazam or Soundhound, but has an API and examples in many languages, making it easy to use.

### spotify.py
ties it all together using Spotipy (http://spotipy.readthedocs.io/en/latest/), which allows you to use the Spotify Web API in Python. I originally tried using the API normally with Javascript but didn't know enough, so Spotipy helped a ton.

# possibilites for the future

-maybe put on a website 
