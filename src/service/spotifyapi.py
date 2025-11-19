import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from Album import Album


def get_albums_for_artist(artist_id: str) -> list[Album]:
    client_id = "<client id>"
    client_secret = "<SECRET>"
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    albums: list[Album] = []
    seen = set()

    results = sp.artist_albums(artist_id, album_type="album")
    while results:
        for item in results["items"]:
            name = item["name"]
            release_date = item["release_date"]
            key = (name, release_date)
            if key in seen:
                continue
            seen.add(key)
            total_tracks = item["total_tracks"]
            year = release_date.split("-")[0]
            download_number = 0
            artist_name = item["artists"][0]["name"]
            imageUrl = item["images"][1]["url"]

            alb = Album(
                artist=artist_name,
                album=name,
                songsNumber=total_tracks,
                year=year,
                downloadNumber=download_number,
                imageUrl=imageUrl
            )
            albums.append(alb)

        if results.get("next"):
            results = sp.next(results)
        else:
            results = None

    return albums

