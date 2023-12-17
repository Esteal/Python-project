import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi import YTMusic

#PARTIE SPOTIFY
client_id = "fda10b209f324dac8aaf840bd7f4688e"
client_secret = "99b55beb11d64c589d7351643b1a3f23"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,
                                               client_secret,
                                               redirect_uri="http://localhost:8888/",
                                               scope="user-library-read"))

#Permet d'enregistrer les titres likés de spotify
offset = 0
spotify_track = []
while True:
    results = sp.current_user_saved_tracks(limit=50, offset=offset)
    if not results['items']:
        break
    for idx, item in enumerate(results['items']):
        track = item['track']
        track_name = track['name']
        track_artiste = track['artists'][0]['name']
        print(idx + offset, track_artiste, " – ", track_name)
        spotify_track.append([track_artiste, track_name]) 
    offset += len(results['items'])

#PARTIE YT MUSIC
ytmusic = YTMusic('oauth.json')

playlist_name = input('Entrez le nom exact de votre playlist ou tapez "like" pour liker les titres : ')
not_find_tracks = []

if playlist_name.lower() == 'like':
    like_songs = True
else:
    like_songs = False
    playlists = ytmusic.get_library_playlists(limit=40)
    for playlist in playlists:
        if playlist['title'] == playlist_name:
            playlist_id = playlist['playlistId']
            break
    else:
        print("Playlist non trouvée.")
        playlist_id = None

# Permet d'ajouter à la playlist souhaité les titres likes
if like_songs:
    for artist, track_name in spotify_track:
        try:
            search_results = ytmusic.search(query=f"{artist} {track_name}", filter="songs")
            if search_results:
                song_id = search_results[0]['videoId']
                ytmusic.rate_song(song_id, 'LIKE')
                print(f"Ajouté aux titres likés : {artist} - {track_name}")
                time.sleep(1)
            else:
                not_find_tracks.append([artist, track_name])
                print(f"Non trouvé sur YouTube Music: {artist} - {track_name}")
        except Exception as e:
            print(f"Erreur lors de l'ajout du morceau {artist} - {track_name}: {e}")
            time.sleep(20)
            not_find_tracks.append([artist, track_name])
            continue
else:
    if playlist_id:
        print("ID de la playlist 'playlist_test':", playlist_id)
        
        playlist_items = ytmusic.get_playlist(playlist_id, limit=5000)['tracks']  # 5000 = nombre de titre grab

        existing_tracks = set()
        for item in playlist_items:
            track_info = f"{item['title']} - {item['artists'][0]['name']}"
            existing_tracks.add(track_info)
        for artist, track_name in spotify_track:
            track_info = f"{track_name} - {artist}"
            if track_info in existing_tracks:
                print(f"Le morceau '{track_info}' est déjà dans la playlist.")
                continue

            try:
                search_results = ytmusic.search(query=f"{artist} {track_name}", filter="songs")
                if search_results:
                    song_id = search_results[0]['videoId']
                    ytmusic.add_playlist_items(playlist_id, [song_id])
                    # Ou utiliser ytmusic.rate_song(track_id, 'LIKE') pour liker le morceau
                    print(f"Ajouté à la playlist 'playlist_test': {artist} - {track_name}")
                    time.sleep(1)  # Pause pour éviter de dépasser les limites de l'API
                else:
                    not_find_tracks.append([artist, track])
                    print(f"Non trouvé sur YouTube Music: {artist} - {track_name}")
            except Exception as e:
                print(f"Erreur lors de l'ajout du morceau {artist} - {track_name}: {e}")
                time.sleep(20)
                not_find_tracks.append([artist, track])
                continue
    else:
        print("Impossible de trouver la playlist "+ playlist_name +". Vérifiez le nom et réessayez.")

if not_find_tracks:
    print("Titres non trouvés ou non ajouté : ")
    for artist, tracks in not_find_tracks:
        print(track, " - ", artist)