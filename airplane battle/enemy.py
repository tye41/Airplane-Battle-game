# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:45:17 2020

@author: Ryan
"""

import pygame
from random import *

class Smallenemy(pygame.sprite.Sprite):
    
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load('images/enemy1.png')
        self.destroy_images=[]
        self.destroy_images.extend([\
         pygame.image.load('images/enemy1_down1.png').convert_alpha(),\
         pygame.image.load('images/enemy1_down2.png').convert_alpha(),\
         pygame.image.load('images/enemy1_down3.png').convert_alpha(),\
         pygame.image.load('images/enemy1_down4.png').convert_alpha()])
        self.rect=self.image.get_rect()
        self.width, self.height=bg_size[0],bg_size[1]
        self.speed=2
        self.active=True
        self.mask=pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top =\
        randint(0,self.width-self.rect.width),randint(-5*self.height,0)
        
        
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
    def reset(self):
        self.active=True
       
        self.rect.left, self.rect.top =\
        randint(0,self.width-self.rect.width),randint(-5*self.height,0)
        
class Midenemy(pygame.sprite.Sprite):
    energy=8
    
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load('images/enemy2.png')
        self.destroy_images=[]
        self.destroy_images.extend([\
         pygame.image.load('images/enemy2_down1.png').convert_alpha(),\
         pygame.image.load('images/enemy2_down2.png').convert_alpha(),\
         pygame.image.load('images/enemy2_down3.png').convert_alpha(),\
         pygame.image.load('images/enemy2_down4.png').convert_alpha()])
    
        self.rect=self.image.get_rect()
        self.width, self.height=bg_size[0],bg_size[1]
        self.speed=1
        self.active=True
        self.mask=pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top =\
        randint(0,self.width-self.rect.width),randint(-10*self.height,self.height)
        self.energy=8
        
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
    def reset(self):
        self.active=True
        self.energy=8
        self.rect.left, self.rect.top =\
        randint(0,self.width-self.rect.width),randint(-10*self.height,self.height)
        
class Bigenemy(pygame.sprite.Sprite):
    energy=20
    
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load('images/enemy3_n1.png')
        self.destroy_images=[]
        self.destroy_images.extend([\
         pygame.image.load('images/enemy3_down1.png').convert_alpha(),\
         pygame.image.load('images/enemy3_down2.png').convert_alpha(),\
         pygame.image.load('images/enemy3_down3.png').convert_alpha(),\
         pygame.image.load('images/enemy3_down4.png').convert_alpha()])
        self.rect=self.image.get_rect()
        self.width, self.height=bg_size[0],bg_size[1]
        self.speed=1
        self.active= True
        self.mask=pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top =\
        randint(0,self.width-self.rect.width),randint(-15*self.height,-5*self.height)
        self.energy=20
        
        
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
    def reset(self):
        self.active=True
        self.energy=20
        self.rect.left, self.rect.top =\
        randint(0,self.width-self.rect.width),randint(-15*self.height,-5*self.height)
    