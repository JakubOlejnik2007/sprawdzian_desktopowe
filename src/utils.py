from PIL import ImageFile, Image

def scaleImage(im: ImageFile, heightTo: int) -> Image:
    
    newWidth = heightTo / im.height * im.width // 1

    
    im = im.resize((int(newWidth), heightTo))
    return im
    
    
    
class COLOR_PALETTE:
    WHITE = "#FFFFFF"
    BG_COLOR = "#2E8B57"
    ACCENT_1 = "#61D918"
    
