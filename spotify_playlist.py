import mysql.connector
import pprint
import sys

import spotipy
import spotipy.util as util

def create_db():
	mydb = mysql.connector.connect(
		host="localhost",
		user="yourusername",
		passwd="yourpassword"
		)

	mycursor = mydb.cursor()
	mycursor.execute("CREATE DATABASE stationSongs")

def create_table():
	mydb = mysql.connector.connect(
		host="localhost",
		user="yourusername",
		passwd="yourpassword",
		database="stationSongs"
)
	mycursor = mydb.cursor()
	mycursor.execute("CREATE TABLE stationsAndsongs (station TEXT, songTitle TEXT, artist TEXT")

def connect_to_spotify():
	import spotipy
	sp = spotipy.Spotify()
	results = sp.search(q='weezer', limit=20)

	for i, t in enumerate(results['tracks']['items']):
		print ' ', i, t['name']

def add_track_playlist():
	if len(sys.argv) > 3:
	    username = sys.argv[1]
	    playlist_id = sys.argv[2]
	    track_ids = sys.argv[3:]
	else:
	    print "Usage: %s username playlist_id track_id ..." % (sys.argv[0],)
	    sys.exit()

	scope = 'playlist-modify-public'
	token = util.prompt_for_user_token(username, scope)

	if token:
	    sp = spotipy.Spotify(auth=token)
	    sp.trace = False
	    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
	    print results
	else:
	    print "Can't get token for", username

	    