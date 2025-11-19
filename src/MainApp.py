import tkinter as tk
from PIL import Image, ImageTk
from utils import scaleImage, COLOR_PALETTE, read_albums

from fonts import get_fonts

from Album import Album


class MainApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        img = [Image.open("../assets/img/obraz.png"), Image.open("../assets/img/obraz2.png"), Image.open("../assets/img/obraz3.png")]
        
        self.images = {
            "vinyl": ImageTk.PhotoImage(img[0]),
            "buttonRight": ImageTk.PhotoImage(scaleImage(img[1], 70)),
            "buttonLeft": ImageTk.PhotoImage(scaleImage(img[2], 70))
        }
        
        ITALIC, BIG, BOLD_20 = get_fonts(self.master)
        
        self.master.configure(background=COLOR_PALETTE.BG_COLOR)
        
        self.master.title("MojeDźwięki, Wtkonał: Jakub Olejnik")
        self.master.geometry("1000x300")
        
        mainLayout = tk.Frame(self.master).pack(fill='x')
        
        tk.Button(mainLayout, image=self.images["buttonLeft"], bg=self.master["bg"], command=lambda: self.change_curr_album(False)).pack(side="left")
        tk.Button(mainLayout, image=self.images["buttonRight"], bg=self.master["bg"], command=lambda: self.change_curr_album()).pack(side="right")
        
        
        
        middleBlockLayout = tk.Frame(mainLayout, bg=self.master["bg"])
        middleBlockLayout.pack(side="left", expand=False)
        
        dataLayout = tk.Frame(middleBlockLayout, bg=self.master["bg"])
        dataLayout.pack(side="top", expand=False)
        
        tk.Label(dataLayout, image=self.images["vinyl"], bg=self.master["bg"]).pack(side="left", padx=10)
        
        detailsLayout = tk.Frame(dataLayout, bg=self.master["bg"])
        detailsLayout.pack(side="left", expand=False)
        
        self.artistLabel = tk.Label(detailsLayout, text="Gorillaz", bg=self.master["bg"], foreground=COLOR_PALETTE.WHITE, font=BIG)
        self.artistLabel.pack(anchor="w")
        
        self.albumLabel = tk.Label(detailsLayout, text="\"The Now Now\"", bg=self.master["bg"], foreground=COLOR_PALETTE.WHITE, font=ITALIC, anchor="w")
        self.albumLabel.pack(anchor="w")
        
        subDetailsLayout = tk.Frame(detailsLayout, bg=self.master["bg"])
        subDetailsLayout.pack(anchor='w')
        
        self.tracksCountLabel = tk.Label(subDetailsLayout, text="11 utworów", bg=self.master["bg"], foreground=COLOR_PALETTE.ACCENT_1)
        self.tracksCountLabel.pack(side="left", padx=10)
        
        self.albumYearLabel = tk.Label(subDetailsLayout, text="2018", bg=self.master["bg"], foreground=COLOR_PALETTE.ACCENT_1)
        self.albumYearLabel.pack(side="right", padx=10)
        
        downloadLayout = tk.Frame(middleBlockLayout, bg=self.master["bg"])
        downloadLayout.pack(anchor='w', pady=10)
        
        self.downloadsLabel = tk.Label(downloadLayout, text="124891728", bg=self.master["bg"], foreground=COLOR_PALETTE.ACCENT_1)
        self.downloadsLabel.pack(side="left", padx=10)
        
        self.downloadButton = tk.Button(downloadLayout, text="Pobierz", bg=COLOR_PALETTE.ACCENT_1, font=BOLD_20, command=lambda: self.update_download())
        self.downloadButton.pack(side="right", padx=10)
        
        self.currAlbumIndex = 0
        self.albums = read_albums("../data/Data.txt")
        
        self.switch_labels_text()
        
        self.pack()
        
    
    def update_download(self):
        self.albums[self.currAlbumIndex].downloadNumber+=1
        self.switch_labels_text()
        
        
    def change_curr_album(self, right=True):
        length = len(self.albums)
        
        self.currAlbumIndex = (self.currAlbumIndex + (-1) ** (int(right)+1)) % length
        
        self.switch_labels_text()

        
    def switch_labels_text(self) -> None:
        
        album = self.albums[self.currAlbumIndex]
        
        self.artistLabel.config(text=album.artist)
        self.albumLabel.config(text=album.album)
        self.tracksCountLabel.config(text=f"{album.songsNumber} utworów")
        self.albumYearLabel.config(text=album.year)
        self.downloadsLabel.config(text=album.downloadNumber)