#2D Text Game

import random, os

window_size = 'mode 50,50'

os.system(window_size)

class Player():
    def __init__(self):
        self.position = (25,25)
        self.sprite = "█"
    
player = Player()


