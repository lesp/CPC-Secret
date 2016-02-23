"""
Pi Birthday Dance Mat Controller
Les Pounder Feb 23 2016
Released Under a Creative Commons CC-BY-SA2.0 Licence

This project uses a cheap USB dance mat from eBay to control

Sounds
Images
Neopixels

"""

import pygame, sys
from pygame.locals import *
import pygame
import time

#Initialise the PyGame Libraries for General use, display and joystick.
pygame.init()
pygame.display.init()
pygame.joystick.init()

#Duration controls the delay between button presses on the dance mat.
duration = 0.2

"""
Created a function to handle displaying an image.
img = The filename of the image, use an absolute reference
caption = The title of the window that appears
w = Width of the window, same as the image.
h = Height of the window, same as the image.
"""
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

"""
This function handles music / sound playback, it will play WAV and MP£ files
"""
def music(audio):
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    #Below: This will play the sound once.
    pygame.mixer.music.play(1)

"""
This function will display any colour in any size window.
Colours are mixed using RGB values 0-255 for each colour.
"""

def colour(r,g,b,w,h):
    background = (r,g,b)
    screen = pygame.display.set_mode((w,h))
    screen.fill((background))
    pygame.display.flip()

"""
This is a sanity check to ensure that there is a dance mat plugged in.
"""
    
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joystick detected")
else:
    my_joystick = pygame.joystick.Joystick(0)
    #Added the print to show that the Dance mat has been discovered.
    print(my_joystick)
    #Initialise the joystick.
    my_joystick.init()

#Main loop, runs forever.
while True:
    #For loop looks for events.
    for event in pygame.event.get():
        #If the event type is a button press.
        if event.type == pygame.JOYBUTTONDOWN:
            #If the button that has been pressed is one of the dance mat buttons.
            #I had to manually detect each button using jstest /dev/input/js0
            if event.button == 0:
                pygame.display.init()
                print("LEFT")
                colour(255,0,0,400,400)
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
            pygame.quit()
