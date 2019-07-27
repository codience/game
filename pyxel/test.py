import numpy as np
import pyxel
from PIL import Image as PilImage

import pprint

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
        self.pos.x = x
        self.pos.y = y
        self.vec = dx
        self.size = size
        self.color = color


class App:
    def __init__(self):
        self.IMG_ID0_X = 60
        self.IMG_ID0_y = 65
        self.IMG_ID0 = 1
        self.IMG_ID1 = 0

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
            pyxel.quit()

        dx = pyxel.mouse_x - self.mcat.pos.x
        dy = pyxel.mouse_y - self.mcat.pos.y
        if dx != 0:
            self.mcat.update(pyxel.mouse_x,pyxel.mouse_y,dx)
        elif dy != 0:
            self.mcat.update(pyxel.mouse_x,pyxel.mouse_y,self.mcat.vec)
        
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            new_ball = Ball()
            print('init new ball.')
            print(new_ball.size)
            if self.mcat.vec > 0:
                new_ball.update(self.mcat.pos.x + cat_W / 2 + 6,
                                self.mcat.pos.y + cat_H / 2,
                                self.mcat.vec, new_ball.size, new_ball.color)
            else:
                new_ball.update(self.mcat.pos.x + cat_W / 2 - 6,
                                self.mcat.pos.y + cat_H / 2,
                                self.mcat.vec, new_ball.size, new_ball.color)
            self.Balls.append(new_ball)
            pprint.pprint(self.Balls)

        ball_count = len(self.Balls)
        for i in range(ball_count):
            if 0 < self.Balls[i].pos.x and self.Balls[i].pos.x < window_W:
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

        if self.mcat.vec > 0:
            pyxel.blt(self.mcat.pos.x, self.mcat.pos.y, self.IMG_ID1, 0, 0, -cat_W, cat_H, 5)
        else:
            pyxel.blt(self.mcat.pos.x, self.mcat.pos.y, self.IMG_ID1, 0, 0, cat_W, cat_H, 5)
 
        for ball in self.Balls:
            pyxel.circ(ball.pos.x, ball.pos.y, ball.size, ball.color)

    # def cat(self):
    #     x = pyxel.mouse_x
    #     y = pyxel.mouse_y
    #     if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
    #         pyxel.blt(x,y,0,0,0,-cat_W,cat_H,5)
    #     else:
    #         pyxel.blt(x,y,0,0,0,cat_W,cat_H,5)

App()