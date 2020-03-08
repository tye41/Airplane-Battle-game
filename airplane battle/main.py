# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 18:57:42 2020

@author: Ryan
"""
import pygame
import sys
import traceback
from pygame.locals import *
import myplane
import enemy
from random import *
import bullet


pygame.init()
pygame.mixer.init()

bg_size= width,height= 480,700
screen=pygame.display.set_mode(bg_size)
pygame.display.set_caption('Airplane Battle')

background=pygame.image.load('images/background.png').convert()

Black=(0,0,0)
Green=(0,255,0)
Red=(255,0,0)
White=(255,255,255)

# 载入音乐


#增加飞机
def add_small_enemies(group1,group2,num):
    for i in range(num):
        e1=enemy.Smallenemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1,group2,num):
    for i in range(num):
        e2=enemy.Midenemy(bg_size)
        group1.add(e2)
        group2.add(e2)
        
def add_big_enemies(group1,group2,num):
    for i in range(num):
        e3=enemy.Bigenemy(bg_size)
        group1.add(e3)
        group2.add(e3)     



def main():
    #生成飞机
    me = myplane.Myplane(bg_size)
    enemies=pygame.sprite.Group()
    
    #生成敌方飞机
    small_enemies=pygame.sprite.Group()
    add_small_enemies(small_enemies,enemies,15)
    
    mid_enemies=pygame.sprite.Group()
    add_mid_enemies(mid_enemies,enemies,4)
    
    big_enemies=pygame.sprite.Group()
    add_big_enemies(big_enemies,enemies,2)
    
   #生成子弹
    bullet1=[]
    bullet1_index=0
    BULLET_NUM=4
    for i in range(BULLET_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midtop))
        
        
    #中弹图片索引
    e1_destroy_index=0
    e2_destroy_index=0
    e3_destroy_index=0
    me_destroy_index=0
    
    
    #统计得分 
    
        
    score_font=pygame.font.Font('font/font.ttf',36)
    
    #暂停游戏
    paused= False
    pause_nor_image=pygame.image.load('images/pause_nor.png').convert_alpha()
    pause_pressed_image=pygame.image.load('images/pause_pressed.png').convert_alpha()
    
    resume_nor_image=pygame.image.load('images/resume_nor.png').convert_alpha()
    resume_pressed_image=pygame.image.load('images/resume_pressed.png').convert_alpha()
    paused_rect=pause_nor_image.get_rect()
    paused_rect.left,paused_rect.top=width-paused_rect.width-10,10
    paused_image=pause_nor_image
    
    #全屏炸弹
    bomb_image=pygame.image.load('images/bomb.png').convert_alpha()
    bomb_rect=bomb_image.get_rect()
    bomb_font=pygame.font.Font('font/font.ttf',48)
    bomb_num= 3
    
    
    clock=pygame.time.Clock()
    
   
    Delay=100
    switch_image = True
    score=0
    
    
    running= True

    while running:
       
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #暂停继续键
            elif event.type == MOUSEBUTTONDOWN:
                if event.button==1 and paused_rect.collidepoint(event.pos):
                    paused=not paused 
            elif event.type == MOUSEMOTION:  
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image=resume_pressed_image
                    else:
                        paused_image=pause_pressed_image
                else:
                     if paused:
                        paused_image=resume_nor_image
                     else:
                        paused_image=pause_nor_image
          #炸弹键              
            elif event.type==KEYDOWN:
                if event.key==K_SPACE:
                    if bomb_num:
                        bomb_num-=1
                        for each in enemies:
                            if each.rect.bottom>0:
                                each.active=False
        
        score_font=pygame.font.Font('font/font.ttf',36)
        screen.blit(background,(0,0))
        
        if not paused:
            #检测键盘操作
            key_pressed=pygame.key.get_pressed()
            
            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()
                
            
            
            #发射子弹
            if not(Delay%10):
                bullet1[bullet1_index].reset(me.rect.midtop)
                bullet1_index=(bullet1_index+1)%BULLET_NUM
                
            #检测是否击中敌机
            for b in bullet1:
                if b.active:
                    b.move()
                    screen.blit(b.image,b.rect)
                    enemy_hit=pygame.sprite.spritecollide(b,enemies,False \
                                ,pygame.sprite.collide_mask)
                if enemy_hit:
                    b.active=False
                    for e in enemy_hit:
                        if e in mid_enemies or e in big_enemies:
                            e.energy-=1
                            if e.energy==0:
                                e.active=False
                        else:
                            e.active=False
            
            
            
            
            
            #绘制敌方飞机
            for each in big_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image,each.rect)
                
                #绘制血槽
                    pygame.draw.line(screen,Black,(each.rect.left,each.rect.top-5),\
                                 (each.rect.right,each.rect.top-5),2)
                
                    energy_remain=each.energy / enemy.Bigenemy.energy
                    if energy_remain>0.2:
                        energy_color=Green
                    else:
                        energy_color=Red
                    pygame.draw.line(screen,energy_color,(each.rect.left,each.rect.top-5),\
                                 (each.rect.left+each.rect.width*energy_remain,\
                                  each.rect.top-5),2)
                
                else:
                    #毁灭
                    while e3_destroy_index < 4:
                        screen.blit(each.destroy_images[e3_destroy_index],each.rect)
                        e3_destroy_index+=1
                    score+=10000
                    each.reset()
                    
            for each in mid_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image,each.rect)
                    
                    pygame.draw.line(screen,Black,(each.rect.left,each.rect.top-5),\
                                 (each.rect.right,each.rect.top-5),2)
                
                    energy_remain=each.energy / enemy.Midenemy.energy
                    if energy_remain>0.2:
                        energy_color=Green
                    else:
                        energy_color=Red
                    pygame.draw.line(screen,energy_color,(each.rect.left,each.rect.top-5),\
                                 (each.rect.left+each.rect.width*energy_remain,\
                                  each.rect.top-5),2)
                else:
                    #毁灭
                    while e2_destroy_index < 4:
                        screen.blit(each.destroy_images[e2_destroy_index],each.rect)
                        e2_destroy_index+=1
                    score+=6000
                    each.reset()
                    
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image,each.rect)
                else:
                    #毁灭
                    while e1_destroy_index < 4:
                        screen.blit(each.destroy_images[e1_destroy_index],each.rect)
                        e1_destroy_index+=1
                    score+=1000
                    each.reset()
            
            
            #检测我方飞机被撞
            enemies_down=pygame.sprite.spritecollide(me,enemies,False,pygame.sprite.collide_mask)
            if enemies_down:
                me.active=False
                for e in enemies_down:
                    e.active=False
            #绘制我方飞机
            if me.active:
                
                screen.blit(me.image, me.rect)
             
            else:
                #毁灭
                while me_destroy_index < 4:
                        screen.blit(me.destroy_images[me_destroy_index],me.rect)
                        me_destroy_index+=1
                running=False
            
            
            #显示炸弹
            bomb_text=bomb_font.render('* %d'%bomb_num,True,White)
            text_rect=bomb_text.get_rect()
            screen.blit(bomb_image,(10,height-10-bomb_rect.height))
            screen.blit(bomb_text,(20+bomb_rect.width,height-5-text_rect.height))
            
            
        score_text=score_font.render('Score : %s' %str(score),True,White)
        screen.blit(score_text,(10,5))
            
            #绘制暂停
        screen.blit(paused_image,paused_rect)
   
        if not(Delay % 5):
            switch_image = not switch_image

        
        Delay-=1
        if not Delay:
            Delay = 100
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit
if __name__=='__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
    
 
