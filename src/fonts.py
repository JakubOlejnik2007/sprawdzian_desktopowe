from tkinter import font

def get_fonts(root):
    ITALIC = font.Font(root=root, family="Arial", size=22, slant="italic")
    BIG_FONT = font.Font(root=root, family="Arial", size=40)
    return ITALIC, BIG_FONT
