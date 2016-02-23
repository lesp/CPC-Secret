#Pygame joypad test

import pygame, sys
from pygame.locals import *
import time
import os

pygame.init()
pygame.display.init()
pygame.joystick.init()

duration = 0.1

def picture(img,w,h):
    pic = pygame.image.load(img)
    background = (255, 64, 64)
    screen = pygame.display.set_mode((w,h))
    screen.fill((background))
    screen.blit(pic,(0,0))
    pygame.display.flip()
    sleep(2)
    pygame.display.quit()
    pygame.quit()

def music(audio):
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play(1)
    

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
                time.sleep(duration)
            elif event.button == 5:
                print("SQUARE")
                time.sleep(duration)
            elif event.button == 6:
                print("X")
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
            pygame.display.quit()
            pygame.quit()
                
    """
    for i in range(joystick_count):
        name = my_joystick.get_name()
        print(name)
        state = my_joystick.get_button(0)
        print(state)
        sleep(0.1)
    """

"""
    for event in pygame.event.get():

        if event.type == pygame.JOYBUTTONDOWN:
            print("Button Pressed")
        elif event.type == pygame.JOYBUTTONUP:
            print("Button Released")
"""

