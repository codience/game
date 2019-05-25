import numpy as np
import pyxel
from PIL import Image as PilImage

window_H = 120
window_W = 160
cat_H = 16
cat_W = 16

class App:
    def __init__(self):
        pyxel.init(window_W,window_H,caption = "Hello pyxel")
        imgs = pyxel.load('./test.pyxel')
        pyxel.run(self.update,self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.puit()
    
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0,0,0,0,0,16,16)
        pyxel.blt(75,45,1,0,0,cat_W,cat_H,5)


App()