from ytmusicapi import YTMusic
from pytube import YouTube
import os
import moviepy.editor as mp

# Initialisation de YTMusic
ytmusic = YTMusic('oauth.json')
liked_songs = ytmusic.get_liked_songs(limit=500)['tracks']

# Création du dossier pour les MP3 si non existant
if not os.path.exists('musique'):
    os.makedirs('musique')

for song in liked_songs:
    song_title = song['title']
    song_artist = song['artists'][0]['name']
    expected_filename = f"{song_title} - {song_artist}.mp3".replace("/", "_").replace("\\", "_")

    # Vérifier si le fichier existe déjà
    if os.path.exists(os.path.join('musique', expected_filename)):
        print(f"Le fichier '{expected_filename}' existe déjà.")
        continue

    try:
        url = f"http://www.youtube.com/watch?v={song['videoId']}"
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        
        output_path = video.download(output_path='musique')
        
        # Convertir en MP3
        base, ext = os.path.splitext(output_path)
        new_file = base + '.mp3'
        clip = mp.AudioFileClip(output_path)
        clip.write_audiofile(new_file)

        # Renommer le fichier MP3
        final_filename = os.path.join('musique', expected_filename)
        os.rename(new_file, final_filename)
        print(f"Téléchargé et converti : {expected_filename}")

    except Exception as e:
        print(f"Erreur lors du téléchargement de {song_title} - {song_artist}: {e}")
    finally:
        # Supprimer le fichier original téléchargé
        # Parfois faire rm *.mp4 dans une cmd car l'algo n'arrive pas à supprimer le fichier
        try:
            os.remove(output_path)
        except Exception as e:
            print("Fichier MP4 non effacé:", e)