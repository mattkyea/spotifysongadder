## What is this?
This is a personal project I worked on during the summer of 2018. I didn't have an internship at the time, and wanted to work on programming projects for fun and to practice using Python to make something practical.

I first thought of trying to make this program after using the app Soundhound on my phone - it allows you to hit a button to identify a song by recording audio from your phone's microphone. This is very useful when you hear a song you like on the radio, but do not know what it is called. The app also has a feature to add the song to your Spotify library once you've identified it. 

So, I knew that it was possible to identify and add a song to your Spotify, and I started working on this program to see if I could replicate this result on my own, and maybe add improvements to it. I also decided to use this program as a way to formally work on my Python skills after completing an online training course. At this point in my college classes, I had only had the opportunity to use C and Java, and wanted to learn Python on my own.

I started by researching systems, tools, and libraries I could use for the three main parts of this program: recording, identification, and adding to Spotify.  

## Recording
I quickly found that PyAudio was a easy and accurate recording library for Python (http://people.csail.mit.edu/hubert/pyaudio/). I followed the documentation on their website to create "recorder.py," which records 10 seconds of audio and saving the file as "file.flac" (which can be slightly better quality than an mp3). This sample will be used to identify the song.

## Identification
Identification was where I reached my first major hurdle - how to apps like Soundhound and Shazam identify a song? At the time, I could not find an API for either system, but as of 2020, Soundhound has an easly available API called Houndify. So, I kept looking for something I could use for free. I eventually came across a service called ACRCloud (https://www.acrcloud.com/docs/acrcloud/tutorials/identify-music-by-sound/), which offered a music recognition tool. I once again followed their example, and created "identify.py," which provided "file.flac" to ACRCloud. ACRCloud returns a JSON containing the song's title, artist, and other information. Most importantly it also provided the song's Spotify ID, which I could use to add the song to a user's library.

## Adding
At this point in the project, I thought the hardest part was over - I successfully recorded and identified the song, and only had to add the song to a user's library. However, I quickly ran into multiple issues with Spotify's API. At the time, it seemed like I needed to use JavaScript to use the API, but I did not yet know JavaScript or how to pass the ID from a Python program to a JavaScript program. So, after much trial and error, I found a library for Python called Spotipy where I could write Python code to communicate with Spotify's API (http://spotipy.readthedocs.io/en/latest/). From here, I created "spotify.py" to add the song to a playlist the program creates in the user's library called "Songs Added from Song Finder." I did by combining a lot of examples on Spotipy's documentation, as I needed to: get authentication from the user, create the playlist if it doesn't exist, then add the song if it wasn't in the playlist already. 


## Basic Flow/ How it Works:

-run "python spotify.py username" with username being your spotify username

-paste the link that pops up in your browser back into the console (this happens twice, and is Spotify's 
authentication - allowing me to read, create, and add to your playlists)

-I check for a playlist titled "Songs Added from Song Finder" in your playlists, creating it if it doesn't exist, then getting its id for later use

-recorder.py is called, recording whatever is playing on your computer (works best with headphone mic)

-identify.py is called with that recording, returning either the song's id, title with artist, or an error

-the id is used to see if the song is already in the playlist (no repeats)

-if the song isn't in the playlist, its added

-the process starts over at recording

## recorder.py
records 10 seconds of audio using PyAudio (http://people.csail.mit.edu/hubert/pyaudio/), saving the file as file.flac (possibly higher quality than mp3). This sample will be used to identify the song.

## identify.py
uses ACRCloud's service (https://www.acrcloud.com/docs/acrcloud/tutorials/identify-music-by-sound/) to identify the recorded audio, returning a title, artist, and Spotify ID if found. Works like Shazam or Soundhound, but has an API and examples in many languages, making it easy to use.

## spotify.py
ties it all together using Spotipy (http://spotipy.readthedocs.io/en/latest/), which allows you to use the Spotify Web API in Python. I originally tried using the API normally with Javascript but didn't know enough, so Spotipy helped a ton.

## Things That Went Well
-Successfully got the program to work

-Was able to practice writing something real in Python

-First time using an API in some sense, and tying together multiple systems/services

## Things That Could Have Gone Better
-Code ended up a little messy, and there's a few points that could be fixed (for example the authentication requires 2 tries when it should only need 1). Once I got something working I left it alone, and should have gone back to see if there were easier or more optimized ways.

-Didn't have enough time afterwards to improve on the idea, like I originally wanted to (add to any playlist, play the song, send the song to someone, etc).

-Knowing a little more about each system would be good - felt like I was in a little over my head and should review the program to learn more about how each service I used works, as well as see if there are other services that would work better today (like using Houndify).

## possibilites for the future
-maybe put on a website or add as a extension to a web browser

-allow user to add to any playlist of theirs

-quicker authentication and identification

-more accurate identification and support for more songs


