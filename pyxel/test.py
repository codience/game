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
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.puit()
    
    def draw(self):
        pyxel.cls(0)
        pyxel.text(55,40,"codience",pyxel.frame_count % 16)
        pyxel.blt(0,0,0,0,0,0,38,16)
        self.cat()

    def cat(self):
        x = pyxel.mouse_x
        y = pyxel.mouse_y
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            pyxel.blt(x,y,0,0,0,-cat_W,cat_H,5)
        else:
            pyxel.blt(x,y,0,0,0,cat_W,cat_H,5)

App()