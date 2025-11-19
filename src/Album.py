class Album:
    def __init__(self, artist, album, songsNumber, year, downloadNumber, imageUrl = None):
        self.artist = artist
        self.album = album
        self.songsNumber = songsNumber
        self.year = year
        self.downloadNumber = int(downloadNumber)
        
        
        self.imageUrl = imageUrl