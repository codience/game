import numpy as np
import pyxel
from PIL import Image as PilImage

window_H = 120
window_W = 160
cat_H = 16
cat_W = 16

class Vec2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class cat:
    def __init__(self,img_id):
        self.pos = Vec2(0,0)
        self.vec = 0
        self.img_cat = img_id
    
    def update(self,x,y,dx):
        self.pos.x = x
        self.pos.y = y
        self.vec = dx


class Ball:
    def __init__(self):
        self.pos = Vec2(0,0)
        self.vec = 0
        self.size = 2
        self.speed = 3
        self.color = 10

    def update(self,x,y,dx,size,color):
        self.pos_x = x
        self.pos_y = y
        self.vec = dx
        self.size = size
        self.color = color


class App:
    def __init__(self):
        self.IMG_ID0_X = 60
        self.IMG_ID0_y = 65
        self.IMG_ID0 = 0
        self.IMG_ID1 = 1

        pyxel.init(window_W,window_H,caption = "Hello pyxel")
        #imgs = pyxel.load('./test.pyxel')

        pyxel.image(self.IMG_ID0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.image(self.IMG_ID1).load(0, 0, "assets/cat_16x16.png")
 
        #pyxel.mouse(True)

        self.mcat = cat(self.IMG_ID1)
        self.Balls = []

        pyxel.run(self.update,self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.puit()

        dx = pyxel.mouse_x - self.mcat.pos.x
        dy = pyxel.mouse.y - self.mcat.pos.y
        if dx != 0:
            self.mcat.update(pyxel.mouse_x,pyxel.mouse_y,dx)
        elif dy != 0:
            self.mcat.update(pyxel.mouse_x,pyxel.mouse.y,self.mcat.vec)
        
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            new_ball = Ball()
            if self.mcat.vec > 0:
                new_ball.update(self.mcat.pos.x + CAT_W / 2 + 6,
                                self.mcat.pos.y + CAT_H / 2,
                                self.mcat.vec, new_ball.size, new_ball.color)
            else:
                new_ball.update(self.mcat.pos.x + CAT_W / 2 - 6,
                                self.mcat.pos.y + CAT_H / 2,
                                self.mcat.vec, new_ball.size, new_ball.color)
            self.Balls.append(new_ball)

        ball_count = len(self.Balls)
        for i in range(ball_count):
            if 0 < self.Balls[i].pos.x and self.Balls[i].pos.x < WINDOW_W:
                if self.Balls[i].vec > 0:
                    self.Balls[i].update(self.Balls[i].pos.x + self.Balls[i].speed, 
                                        self.Balls[i].pos.y, 
                                        self.Balls[i].vec, self.Balls[i].size, self.Balls[i].color)
                else:
                    self.Balls[i].update(self.Balls[i].pos.x - self.Balls[i].speed, 
                                        self.Balls[i].pos.y, 
                                        self.Balls[i].vec, self.Balls[i].size, self.Balls[i].color)
            else:
                del self.Balls[i]
                break

    
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