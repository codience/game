import pyxel
import random

class App:
    def __init__(self):
        pyxel.init(100, 100)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x+1.3) % pyxel.width

    def draw(self):
        pyxel.cls(6)
        pyxel.rect(self.x, random.randint(0, 100), self.x+15, 0, 2)

App()