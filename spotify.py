import sys
import pprint
import os
import subprocess
import spotipy
import spotipy.util as util
import simplejson as json
from identify import identify
from recorder import record

def getPlaylists(username,token,sp):
    results = sp.current_user_playlists()
    exists = False
    ret = 0
    for i, item in enumerate(results['items']):
        #print(item['name'])
        name = item['name']
        playlistid = item['id']
        if "Songs Added from Song Finder" == name:
            ret = playlistid
            exists = True
    if exists == False:
        print("create")
        createPlaylist(username)
        ret = getPlaylists(username,token,sp)
    else:
        print("aready there")
    return ret

def newToken(username):
    scope = 'playlist-modify-private'
    token = util.prompt_for_user_token(username,scope,client_id='f77b6cd7d458455e8e0671da6eacb58b',client_secret='363177e753b74177b167a25d9831fc6f',redirect_uri='http://localhost:8888/callback')
    sp = spotipy.Spotify(auth=token)
    return sp

def createPlaylist(username):
    sp = newToken(username)
    playlists = sp.user_playlist_create(username, "Songs Added from Song Finder",public=False)
    #pprint.pprint(playlists)

def getSong(username,token,sp):
    print("record, identify, return id")
    #os.system("python recorder.py")
    #os.system("python identify.py file.flac")
    record()
    return identify()

def checkSong(username,token,sp,songid,playlistid):
    print("lets check if the song is already in the playlist, or not on spotify")
    if "Song not on Spotify" in songid:
        print(songid)
    else:
        print("check")
        songs = sp.user_playlist(username, playlistid,'tracks')
        songs = str(songs)
        if songid in songs:
            print("song already in playlist")
        else:
            addSong(username,token,sp,songid,playlistid)

def addSong(username,token,sp,songid,playlistid):
    ids = [songid]
    sp.user_playlist_add_tracks(username, playlistid, ids)
    print("song added")

def main():
    scope = 'playlist-read-private'

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: %s username" % (sys.argv[0],))
        sys.exit()

    token = util.prompt_for_user_token(username,scope,client_id='f77b6cd7d458455e8e0671da6eacb58b',client_secret='363177e753b74177b167a25d9831fc6f',redirect_uri='http://localhost:8888/callback')

    if token:
        sp = spotipy.Spotify(auth=token)
        playlistid = getPlaylists(username,token,sp)
        print(playlistid)
        sp = newToken(username)
        while True:
            response = input("1 to record, 0 to quit\n")
            if response == "1":
                songid = getSong(username,token,sp)
                if songid == "error recording song":
                    print("error recording/identifying song")
                else:
                    checkSong(username,token,sp,songid,playlistid)
            elif response == "0":
                print("bye!")
                break
            else: 
                print("invalid command")
    else:
        print ("Can't get token for", username)

if __name__ == "__main__":
    main()