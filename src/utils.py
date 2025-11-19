from PIL import ImageFile, Image
from Album import Album

def scaleImage(im: ImageFile, heightTo: int) -> Image:
    
    newWidth = heightTo / im.height * im.width // 1

    
    im = im.resize((int(newWidth), heightTo))
    return im
    
    
    
class COLOR_PALETTE:
    WHITE = "#FFFFFF"
    BG_COLOR = "#2E8B57"
    ACCENT_1 = "#61D918"
    
    

def read_albums(fileStr: str) -> list[Album]:
    with open(fileStr, "r") as file:
        lines = file.readlines()
        
        albums = []
        
        curr_alb = []
        
        for line in lines:
            line = line.strip()
            if line == "":
                artist, album, songsNumber, year, downloadNumber = curr_alb
        
                albums.append(Album(artist, album, songsNumber, year, downloadNumber))
                curr_alb = []
                continue
        
            
            curr_alb.append(line)
        return albums