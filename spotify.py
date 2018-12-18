import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from terminal
username = '22cg5niqe2hfgk6bn3sybefdq'
playlist_id = '0RTmSKHdhW3n842J1rRUKD'
scope = 'playlist-modify-public'


# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope) # add scope

if token:
    spotify = spotipy.Spotify(auth=token)
    track_ids = []
    #get the file & read it line by line
    with open('spotifyPlaylist.txt', 'r') as f:
        for line in f:
            [artist, track] = line.split(',')
            track_id = spotify.search(q='artist:' + artist + ' track:' + track, type='track')
            print(track_id.tracks)
            track_ids.append(track_id)
#            print(json.dumps(track_id, sort_keys=True,indent=4))
    results = spotify.user_playlist_add_tracks(username, playlist_id, track_ids)
else:
    print("Can't get token for", username)

#Rita Ora, Let You Love Me
#Ed Sheeran, Perfect
#lovelytheband, broken
#Sean Paul, Temperature
#NF, Lie
#Cheat Codes, No Promises (feat. Demi Lovato)
#Bazzi, Beautiful (feat. Camila Cabello)
#MAX, Lights Down Low
#Dan + Shay, Tequila

#results = spotify.user_playlist_add_tracks(username, playlist_id, track_ids)
#if artist != "":
#    print("Currently playing " + artist + " - " + track)


## Get current device
#devices = spotifyObject.devices()
#deviceID = devices['devices'][0]['id']
#
## Current track information
#track = spotifyObject.current_user_playing_track()
#artist = track['item']['artists'][0]['name']
#track = track['item']['name']
#

#

## Loop
#while True:
#    # Main Menu
#    print()
#    print(">>> Welcome to Spotipy " + displayName + "!")
#    print(">>> You have " + str(followers) + " followers.")
#    print()
#    print("0 - Search for an artist")
#    print("1 - exit")
#    print()
#    choice = input("Your choice: ")
#
#    if choice == "0":
#        print()
#        searchQuery = input("Ok, what's their name?: ")
#        print()
#
#        # Get search results
#        searchResults = spotifyObject.search(searchQuery,1,0,"artist")
#
#        # Artist details
#        artist = searchResults['artists']['items'][0]
#        print(artist['name'])
#        print(str(artist['followers']['total']) + " followers")
#        print(artist['genres'][0])
#        print()
#        webbrowser.open(artist['images'][0]['url'])
#        artistID = artist['id']
#
#
#        # Album and track details
#        trackURIs = []
#        trackArt = []
#        z = 0
#
#        # Extract album data
#        albumResults = spotifyObject.artist_albums(artistID)
#        albumResults = albumResults['items']
#
#        for item in albumResults:
#            print("ALBUM: " + item['name'])
#            albumID = item['id']
#            albumArt = item['images'][0]['url']
#
#            # Extract track data
#            trackResults = spotifyObject.album_tracks(albumID)
#            trackResults = trackResults['items']
#
#            for item in trackResults:
#                print(str(z) + ": " + item['name'])
#                trackURIs.append(item['uri'])
#                trackArt.append(albumArt)
#                z+=1
#            print()
#
#    # See album art
#    while True:
#        songSelection = input("Enter a song number to see album art and play the song (x to exit): ") # and play the song
#        if songSelection == "x":
#            break
#            trackSelectionList = []
#            trackSelectionList.append(trackURIs[int(songSelection)])
#            spotifyObject.start_playback(deviceID, None, trackSelectionList) # added
#            webbrowser.open(trackArt[int(songSelection)])
#
#if choice == "1":
#    break
#
## print(json.dumps(trackResults, sort_keys=True, indent=4))
