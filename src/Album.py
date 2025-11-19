class Album:
    def __init__(self, artist, album, songsNumber, year, downloadNumber):
        self.artist = artist
        self.album = album
        self.songsNumber = songsNumber
        self.year = year
        self.downloadNumber = int(downloadNumber)
        