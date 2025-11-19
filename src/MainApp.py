import tkinter as tk
from PIL import Image, ImageTk

class MainApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        img = [Image.open("../assets/img/obraz.png"), Image.open("../assets/img/obraz2.png"), Image.open("../assets/img/obraz.png")]
        
        self.images = {
            "vinyl": ImageTk.PhotoImage(img[0]),
            "buttonLeft": ImageTk.PhotoImage(img[1]),
            "buttonRight": ImageTk.PhotoImage(img[2])
        }
        
        
        
        self.master.configure(background="#2E8B57")
        self.master.title("MojeDźwięki, Wtkonał: Jakub Olejnik")
        self.master.geometry("1000x400")
        
        
        mainLayout = tk.Frame(self.master).pack()
        
        tk.Button(mainLayout, text="<<").pack(side="left")
        tk.Button(mainLayout, text=">>").pack(side="right")
        
        tk.Button(mainLayout, text="^^").pack(side="left")
        
        tk.Label(mainLayout, image=self.images["winyl"], bg=self.master["bg"]).pack(side="left")
        
        
        
        
        
        self.pack()