from typing import Any
from pygame import *
from random import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

Game_room = 'room_1'
abcd = True
finish = False
clr =((0,255,0))
pic = image.load("start_room.jpeg")
display.set_caption("isaac")
window = display.set_mode((700,500))
bg = transform.scale(pic, (700,500))

class GameSprite (sprite.Sprite):
    def __init__(self,picture,width,height,x,y):
        super().__init__()
        self.image=transform.scale(image.load(picture),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset (self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Bullet(GameSprite):
    def __init__ (self,picture,width,height,x,y,speed,goal):
        super().__init__(picture,width,height,x,y)
        self.x_speed = ((goal.rect.x - self.rect.x) * speed) / ((goal.rect.x ** 2 + goal.rect.y ** 2) ** 0.5)
        self.y_speed = ((goal.rect.y - self.rect.y) * speed) / ((goal.rect.x ** 2 + goal.rect.y ** 2) ** 0.5)
        self.goal = goal

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.x > 700 or self.rect.x < 0 or self.rect.y > 500 or self.rect.y < 0:
            self.kill()

class Player(GameSprite):
    def __init__ (self,picture,width,height,x,y,x_speed,y_speed):
        super().__init__(picture,width,height,x,y)
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.hp = 5
    def update(self):
        old_x = self.rect.x
        old_y = self.rect.y
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        for p in platforms_touched:
            if self.x_speed > 0:
                self.rect.right = p.rect.left
            elif self.x_speed < 0:
                self.rect.left = p.rect.right
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        for p in platforms_touched:
            if self.y_speed > 0:
                self.rect.bottom = p.rect.top
            elif self.y_speed < 0:
                self.rect.top = p.rect.bottom
        if self.rect.x < 80:
            self.rect.x = 80
        if self.rect.x > 580:
            self.rect.x = 580
        if self.rect.y < 80:
            self.rect.y = 80
        if self.rect.y > 360:
            self.rect.y = 359
    def fire(self):
        bulet = Bullet("bulet.png",13,13,self.rect.centerx,self.rect.centery,10,boss)
        bulets.add(bulet)
            
class Enemy(GameSprite):
    def __init__ (self,picture,width,height,x,y,speed,):
        super().__init__(picture,width,height,x,y)
        self.speed = speed
        self.direction = "left"
    def update(self):
        if self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        elif self.rect.x < player.rect.x:
            self.rect.x += self.speed
        if self.rect.y > player.rect.y:
            self.rect.y -= self.speed
        elif self.rect.y < player.rect.y:
            self.rect.y += self.speed

class Enemy2(GameSprite):
    def __init__ (self,picture,width,height,x,y,speed,):
        super().__init__(picture,width,height,x,y)
        self.speed = speed
        self.direction = "left"
    def update(self):
        if self.rect.x <= 175:
            self.direction = "right"
        if self.rect.x >= 450:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Boss(GameSprite):
    def __init__ (self,picture,width,height,x,y):
        super().__init__(picture,width,height,x,y)
        self.hp = 25
    def fire(self):
        bulet = Bullet("bulet_red.png",13,13,self.rect.centerx,self.rect.centery,10,player)
        bulets.add(bulet)




barriers = sprite.Group()
wall1 = GameSprite("stone.png",55,55,149,355)
wall2 = GameSprite("stone.png",55,55,149,300)
wall3 = GameSprite("stone.png",55,55,149,245)
wall4 = GameSprite("stone.png",55,55,149,195)
wall5 = GameSprite("stone.png",55,55,149,140)
wall6 = GameSprite("stone.png",55,55,270,85)
wall7 = GameSprite("stone.png",55,55,270,140)
wall8 = GameSprite("stone.png",55,55,270,195)
wall9 = GameSprite("stone.png",55,55,270,245)
wall10 = GameSprite("stone.png",55,55,270,300)
wall11 = GameSprite("stone.png",55,55,560,300)
wall12 = GameSprite("stone.png",55,55,395,300)
wall13 = GameSprite("stone.png",55,55,450,300)
wall14 = GameSprite("stone.png",55,55,505,300)
wall15 = GameSprite("stone.png",55,55,325,165)
wall16 = GameSprite("stone.png",55,55,380,165)
wall17 = GameSprite("stone.png",55,55,435,165)
wall18 = GameSprite("stone.png",55,55,490,165)
barriers.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,wall17,wall18)
player = Player("isaac.png",51,50,95,340,0,0)
enemy = sprite.Group()
enemy1 = Enemy("enemy.png",40,40,85,350,2)
enemy2 = Enemy("enemy.png",40,40,560,350,2)
enemy3 = Enemy2("enemy.png",40,40,175,125,5)
enemy.add(enemy1,enemy2,enemy3)
boss = Boss("boss.png",160,100,270,65)
final_sprite = GameSprite("exit.png",80,65,310,25)
bulets = sprite.Group()

font.init()
font1 = font.SysFont('Arial', 35)

while abcd:
    time.delay(40)
    for i in event.get():
        if i.type == QUIT:
            abcd = False
        elif i.type == KEYDOWN:
            if i.key == K_s:
                player.y_speed=5
            elif i.key == K_w:
                player.y_speed=-5
            elif i.key == K_a:
                player.x_speed=-5
            elif i.key == K_d:
                player.x_speed=5
            elif i.key == K_SPACE:
                if Game_room == 'room_3':
                    player.fire()
        elif i.type == KEYUP:
            if i.key == K_a or i.key == K_d:
                player.x_speed = 0
            elif i.key == K_w or i.key == K_s:
                player.y_speed = 0

    if finish == False:
        window.blit(bg,(0,0))
        player.update()
        player.reset()

        if Game_room == 'room_1':
            final_sprite.reset()
            barriers.draw(window)
            if sprite.collide_rect(player,final_sprite):
                Game_room = "room_2"
                player.rect.x = 310
                player.rect.y = 340
                
        if Game_room == 'room_2':
            final_sprite.reset()
            barriers.empty()  
            enemy.draw(window)
            enemy.update()
            if sprite.collide_rect(player,final_sprite):
                Game_room = "room_3"
                player.rect.x = 310
                player.rect.y = 340
            elif sprite.spritecollide(player,enemy,False):
                Game_room = 'room_defeat'

        if Game_room == 'room_3':
            if player.hp == 0:
                Game_room = 'room_defeat'
            final_sprite.reset()
            bulets.update()
            bulets.draw(window)
            qwe = font1.render('hp '+str(player.hp), True, (0, 165, 0))
            window.blit(qwe,(player.rect.x,player.rect.bottom))
            if boss.hp > 0:
                lose = font1.render('Boss hp '+str(boss.hp), True, (165, 0, 0))
                window.blit(lose,(0,0))
                boss.reset()
                if randint(0,20) == 0:
                    boss.fire()
            elif boss.hp <= 0:
                boss = Boss("boss.png",160,100,100000,65)
                boss.hp = -1
                boss.update()
            if sprite.collide_rect(player,boss):
                Game_room = "room_defeat"
            if sprite.collide_rect(player,final_sprite):
                Game_room = "room_win"
            for bulet in bulets:
                if bulet.goal == player:
                    if sprite.collide_rect(player,bulet):
                        bulet.kill()
                        player.hp -= 1
                if bulet.goal == boss:
                    if sprite.collide_rect(boss,bulet):
                        bulet.kill()
                        boss.hp -= 1

        if Game_room == "room_defeat":
            pic = image.load("defeat.jpg")
            bg = transform.scale(pic, (700,500))
            player.rect.x = 310
            player.rect.y = 340
        if Game_room == "room_win":
            pic = image.load("win.jpg")
            bg = transform.scale(pic, (700,500))
            player.rect.x = 310
            player.rect.y = 340
    display.update()