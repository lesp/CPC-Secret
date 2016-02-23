#Pygame joypad test

import pygame, sys
from pygame.locals import *
import pygame
import time
import os

pygame.init()
pygame.display.init()
pygame.joystick.init()

duration = 0.2

def picture(img,caption,w,h):
    pic = pygame.image.load(img)
    background = (255, 64, 64)
    pygame.display.set_caption(caption)
    screen = pygame.display.set_mode((w,h))
    screen.fill((background))
    screen.blit(pic,(0,0))
    #pygame.display.flip()
    pygame.display.update()
    time.sleep(duration)
    #pygame.display.quit()
    #pygame.quit()

def music(audio):
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play(1)

#def colour(r,g,b):
    
    

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joystick detected")
else:
    my_joystick = pygame.joystick.Joystick(0)
    print(my_joystick)
    my_joystick.init()


while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                pygame.display.init()
                print("LEFT")
                music("/home/les/sonic-pi/etc/samples/drum_cymbal_open.wav")
                time.sleep(duration)
            elif event.button == 1:
                print("DOWN")
                music("/home/les/sonic-pi/etc/samples/drum_tom_lo_hard.wav")
                time.sleep(duration)
            elif event.button == 2:
                print("UP")
                music("/home/les/sonic-pi/etc/samples/drum_heavy_kick.wav")
                time.sleep(duration)
            elif event.button == 3:
                print("RIGHT")
                music("/home/les/sonic-pi/etc/samples/drum_snare_hard.wav")
                time.sleep(duration)
            elif event.button == 4:
                print("TRIANGLE")
                picture("/home/les/Desktop/FreeHugs11-26-2013-2.jpg","FREE HUGS",1000,708)
                time.sleep(duration)
            elif event.button == 5:
                print("SQUARE")
                time.sleep(duration)
            elif event.button == 6:
                print("X")
                picture("/home/les/Desktop/CAT400x400.png","Space Cat",400,400)
                time.sleep(duration)
            elif event.button == 7:
                print("O")
                time.sleep(duration)
            elif event.button == 8:
                print("SELECT")
                time.sleep(duration)
            elif event.button == 9:
                print("START")
        elif event.type == pygame.QUIT:
            print("EXIT")
        #    pygame.display.quit()
            pygame.quit()
