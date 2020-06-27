import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# HTML opening
with open('spotify_search.html', 'a') as other_file:
    opening = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="spotify_search_styling.css"/>
<link href="https://fonts.googleapis.com/css?family=Indie+Flower|Nanum+Brush+Script|New+Rocker|Rock+Salt&display=swap" rel="stylesheet">
</head>
<body>'''
    other_file.write(opening)

# Top Tracks
def top_tracks(spotify):
    artist = input("Which artist's top tracks would you like to view?")
    search_artist_top_tracks = spotify.search(artist)
    artist_id = search_artist_top_tracks['tracks']['items'][0]['artists'][0]['id']
    results = spotify.artist_top_tracks(artist_id, country='US')
    artist_top_tracks = results['tracks']
    with open('spotify_search.html', 'a') as other_file:
        other_file.write("<h1>{}'s top tracks:</h1><ul>".format(artist))
        for artist_top_tracks in artist_top_tracks:
            top = artist_top_tracks['name']
            other_file.write('<li>' + top + '</li>')
        other_file.write("</ul>")
top_tracks(spotify)

# Album Catalogue
def album_search(spotify):
    artist = input("Which artist's albums would you like to find?")
    search_artist = spotify.search(artist)
    artist_uri = search_artist['tracks']['items'][0]['artists'][0]['uri']
    results = spotify.artist_albums(artist_uri, album_type='album', country='US', limit=20, offset=0)
    artist_results = results['items']
    with open('spotify_search.html', 'a') as other_file:
        other_file.write("<h1>{}'s albums:<h1><ul>".format(artist))
        for i in artist_results:
            name = i['name']
            other_file.write('<li>' + name + '</li>')
        other_file.write("</ul>")
album_search(spotify)

# Album basic info

def album_basic_info(spotify):
    album = input('Which album are you looking for?')
    search_album = spotify.search(album)
    album_cover = search_album['tracks']['items'][0]['album']['images'][1]['url']
    with open('spotify_search.html', 'a') as other_file:
        other_file.write(album + "<br>")
        other_file.write('<img src="{}">'.format(album_cover))
        release_date = search_album['tracks']['items'][0]['album']['release_date']
        other_file.write("<h2>{} was released: {}</h2><br>".format(album, release_date))
        album_id = search_album['tracks']['items'][0]['album']['uri']
        tracks = spotify.album_tracks(album_id, limit=50, offset=0)['items']
        other_file.write("<h2>{}'s tracks are:</h2><ol>".format(album))
        for track in tracks:
            other_file.write("<li>" + track['name'] + '</li>')
        other_file.write("</ol>")

album_basic_info(spotify)

# HTML closing
with open('spotify_search.html', 'a') as other_file:
    closing = '''</body>
</html>'''
    other_file.write(closing)