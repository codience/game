import numpy as np
import pyxel
from PIL import Image as PilImage
from time import sleep
import pprint
import random

window_H = 120
window_W = 160
cat_H = 14
cat_W = 14
enemy_H = 12
enemy_W = 18

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

class enemy:
    def __init__(self,img_id):
        self.pos = Vec2(0, 0)
        self.vec = 0
        self.speed = 0.01
        self.img_enemy = img_id

    def update(self, x, y, dx):
        self.pos.x = x
        self.pos.y = y
        self.vec = dx


class App:
    def __init__(self):
        self.IMG_ID0_X = 60
        self.IMG_ID0_y = 65
        self.IMG_ID0 = 1
        self.IMG_ID1 = 0
        self.IMG_ID2 = 2
        self.SOUND_1 = 10
        self.gameover = False
        self.clear = False
        self.clear_flag = False
        self.lucky_flag = False
        self.clear_message = None
        self.lucky_massage = "Lucky Point!!"
        self.now_flame = 0
        self.lucky = False
        self.kill_num = 0
        self.OK = True
        self.ready = False


        pyxel.init(window_W,window_H,caption = "Hello pyxel")

        pyxel.load('./a.pyxel')

        pyxel.image(self.IMG_ID0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.image(self.IMG_ID1).load(0, 0, "assets/cat_16x16.png")
        pyxel.image(self.IMG_ID2).load(0, 0, "assets/mouse.gif")


 
        #pyxel.mouse(True)

        self.mcat = cat(self.IMG_ID1)
        self.Balls = []
        self.enemies = []

        #self.flag = 1
        self.Gameover_flag = 0

        self.score1 = 0

        pyxel.play(1, 1)
        pyxel.play(0, [0,6,7,2,3,2,4,5])

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

        # if self.flag == 1:
        #     new_enemy = enemy(self.IMG_ID2)
        #     new_enemy.update(window_W / 2, window_H / 2 + 30, self.mcat.vec)
        #     self.enemies.append(new_enemy)
            
        #     new_enemy = enemy(self.IMG_ID2)
        #     new_enemy.update(window_W/2 + 30, window_H/2 + 30, self.mcat.vec)
        #     self.enemies.append(new_enemy)
            
        #     new_enemy = enemy(self.IMG_ID2)
        #     new_enemy.update(window_W/2 - 30, window_H/2 + 30, self.mcat.vec)
        #     self.enemies.append(new_enemy)
            
        #     new_enemy = enemy(self.IMG_ID2)
        #     new_enemy.update(window_W/2 - 60, window_H/2 + 30, self.mcat.vec)
        #     self.enemies.append(new_enemy)
                

        if pyxel.frame_count % 30 == 1:
            #from right
            new_enemy = enemy(self.IMG_ID2)
            new_enemy.update(random.randint(window_W, window_W + 5), random.randint(0, window_H + 5), -self.mcat.vec)
            self.enemies.append(new_enemy)
            #from left
            new_enemy = enemy(self.IMG_ID2)
            new_enemy.update(random.randint(-5, 0), random.randint(0, window_H + 5), -self.mcat.vec)
            self.enemies.append(new_enemy)

            #self.flag = 0

        enemy_count = len(self.enemies)
        for i in range(enemy_count):
            ex = (self.mcat.pos.x - self.enemies[i].pos.x)
            ey = (self.mcat.pos.y - self.enemies[i].pos.y)
            kp = self.enemies[i].speed
            if ex != 0 or ey != 0:
                self.enemies[i].update(self.enemies[i].pos.x + ex * kp,
                                        self.enemies[i].pos.y + ey * kp,
                                        self.mcat.vec)

            #当たり判定（敵キャラと猫）
            if ((self.mcat.pos.x < self.enemies[i].pos.x + enemy_W)
                and (self.enemies[i].pos.x + enemy_W < self.mcat.pos.x + cat_W - 7 )
                and (self.mcat.pos.y < self.enemies[i].pos.y + enemy_H)
                and (self.enemies[i].pos.y + enemy_H < self.mcat.pos.y + cat_H - 7 ) 
                or (self.mcat.pos.x < self.enemies[i].pos.x)
                and (self.enemies[i].pos.x < self.mcat.pos.x + cat_W)
                and (self.mcat.pos.y < self.enemies[i].pos.y + enemy_H)
                and (self.enemies[i].pos.y + enemy_H < self.mcat.pos.y + cat_H - 7 )
                or (self.mcat.pos.x < self.enemies[i].pos.x + enemy_W)
                and (self.enemies[i].pos.x + enemy_W < self.mcat.pos.x + cat_W - 7 )
                and (self.mcat.pos.y < self.enemies[i].pos.y)
                and (self.enemies[i].pos.y < self.mcat.pos.y + cat_H - 7 )
                or (self.mcat.pos.x < self.enemies[i].pos.x)
                and (self.enemies[i].pos.x < self.mcat.pos.x + cat_W - 7 )
                and (self.mcat.pos.y < self.enemies[i].pos.y)
                and (self.enemies[i].pos.y < self.mcat.pos.y + cat_H - 7 )):
                self.Gameover_flag = 1

        if pyxel.btnp(pyxel.KEY_Z) and self.OK == True:
            self.kill_num = 0
            new_ball = Ball()
            self.OK = False
            self.ready = True
            pyxel.play(3, 10, loop=False)
            if self.mcat.vec > 0:
                new_ball.update(self.mcat.pos.x + cat_W / 2 + 6,
                                self.mcat.pos.y + cat_H / 2,
                                self.mcat.vec, new_ball.size, new_ball.color)
            else:
                new_ball.update(self.mcat.pos.x + cat_W / 2 - 6,
                                self.mcat.pos.y + cat_H / 2,
                                self.mcat.vec, new_ball.size, new_ball.color)
            self.Balls.append(new_ball)



        if self.OK == False and self.ready == True:
            self.ready = False
            self.now_flame = pyxel.frame_count

        if pyxel.frame_count > self.now_flame + 20:
            self.OK = True    

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
                
                enemy_count = len(self.enemies)
                for j in range(enemy_count):
                    if ((self.enemies[j].pos.x < self.Balls[i].pos.x)
                        and (self.Balls[i].pos.x < self.enemies[j].pos.x + enemy_W)
                        and (self.enemies[j].pos.y < self.Balls[i].pos.y)
                        and (self.Balls[i].pos.y < self.enemies[j].pos.y + enemy_H)):

                        del self.enemies[j] # Balls[i]の座標と合致したenemies[j]をdelete2
                        self.kill_num += 1
                        if not self.Gameover_flag:
                            self.score1 += self.kill_num * 100 # score加算
                            if self.kill_num > 1:
                                pyxel.play(2,9)
                            # 敵を倒して、スコアを加算したあとの処理
                            if random.randint(1, 100) == 1: # 1パーセント
                                self.lucky_message = "Lucky Point!!"
                                self.lucky_flag = True
                                self.lucky = True

                        break
                        
            else:
                del self.Balls[i]
                ball_count -= 1
                break

    
    def draw(self):
        pyxel.cls(0)
        pyxel.text(55,40,"codience",pyxel.frame_count % 16)
        pyxel.blt(0,0,0,0,0,0,38,16)
        
        #score
        score_x = 2
        score_y = window_H - 8
        score = "SCORE:" + str(self.score1)
        pyxel.text(score_x, score_y, score, pyxel.frame_count % 16)

        #cat
        if self.mcat.vec > 0:
            pyxel.blt(self.mcat.pos.x, self.mcat.pos.y, self.IMG_ID1, 0, 0, -cat_W, cat_H, 5)
        else:
            pyxel.blt(self.mcat.pos.x, self.mcat.pos.y, self.IMG_ID1, 0, 0, cat_W, cat_H, 5)
 
        #ball
        for Ball in self.Balls:
            pyxel.circ(Ball.pos.x, Ball.pos.y, Ball.size, Ball.color)

        #enemy
        for enemy in self.enemies:
            if enemy.vec > 0:
                pyxel.blt(enemy.pos.x, enemy.pos.y, enemy.img_enemy, 0, 0, -enemy_W, enemy_H, 11)
            else:
                pyxel.blt(enemy.pos.x, enemy.pos.y, enemy.img_enemy, 0, 0, enemy_W, enemy_H, 11)

        #game over
        if self.Gameover_flag == 1:
            pyxel.text(self.mcat.pos.x - 10, self.mcat.pos.y - 5, "Game Over", 8)
            pyxel.stop()
            if self.gameover == False:
                self.now_flame = pyxel.frame_count
                self.gameover = True
            if pyxel.frame_count > self.now_flame + 20:
                pyxel.quit()

        if self.score1 >= 100000:
            self.clear_message = "Clear!!"
            self.clear_flag = True

        if self.clear_flag == True:
            self.raise_clear(clear_text = self.clear_message)
        
        if self.lucky_flag == True:
            self.raise_lucky(lucky_text = self.lucky_massage)

    def raise_clear(self, clear_text):
        pyxel.text(self.mcat.pos.x - 10, self.mcat.pos.y - 5, clear_text, 8)
        pyxel.stop()
        if self.clear == False:
            self.now_flame = pyxel.frame_count
            self.clear = True
        if pyxel.frame_count > self.now_flame + 20:
            pyxel.quit()
    
    def raise_lucky(self, lucky_text):
        pyxel.text(self.mcat.pos.x - 10 , self.mcat.pos.y - 5, lucky_text, 8)
        self.score1 += 30000
        self.lucky = False
        self.lucky_flag = False

        #if self.lucky == True:
        #    self.lucky = False
        #    self.now_flame = pyxel.frame_count
        #    if pyxel.frame_count > self.now_flame + 20:
        #        self.lucky_flag = False
        


   
App()