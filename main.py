#2D Text Game

import random, os

window_size = 'mode 50,20'

os.system(window_size)

class Player():
    def __init__(self):
        self.position = (25,10)
        self.sprite = "█"
    
player = Player()
