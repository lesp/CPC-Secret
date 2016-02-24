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
from neopixel import *


# LED strip configuration:
LED_COUNT      = 240      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 32     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)



#Initialise the PyGame Libraries for General use, display and joystick.
pygame.init()
pygame.display.init()
pygame.joystick.init()

#Duration controls the delay between button presses on the dance mat.
duration = 0.2

def colorWipe(strip, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()):
                strip.setPixelColor(i, color)
                strip.show()
                #time.sleep(wait_ms/1000000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			#time.sleep(wait_ms/10000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

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

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

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
                theaterChase(strip, Color(127, 127, 127)) #WHITE
                music("samples/drum_cymbal_open.wav")
                picture("images/cymbals.jpg","cymballs",1430,1200)
                time.sleep(duration)
            elif event.button == 1:
                print("DOWN")
                theaterChase(strip, Color(255, 0, 0)) #RED
                music("samples/drum_tom_lo_hard.wav")
                picture("images/snare-drum.jpg","Drum",920,640)
                time.sleep(duration)
            elif event.button == 2:
                print("UP")
                theaterChase(strip, Color(0, 255, 0)) #Green
                music("samples/drum_heavy_kick.wav")
                picture("images/kick-drum.jpg","Kick Drum",292,300)
                time.sleep(duration)
            elif event.button == 3:
                print("RIGHT")
                theaterChase(strip, Color(0, 0, 255)) #BLUE
                music("samples/drum_snare_hard.wav")
                picture("images/snare-drum.jpg","Drum",920,640)
                time.sleep(duration)
            elif event.button == 4:
                print("TRIANGLE")
                theaterChase(strip, Color(255, 0, 255)) #PURPLE
                music("samples/loop_amen.wav")
                picture("images/lsp.jpg","Erh my glob!",500,375)
                time.sleep(duration)
            elif event.button == 5:
                print("SQUARE")
                theaterChase(strip, Color(255, 255, 0)) #RED
                music("samples/bd_boom.wav")
                picture("images/raspberry-pi-logo.jpg","Raspberry Pi!",900,450)
                time.sleep(duration)
            elif event.button == 6:
                print("X")
                theaterChase(strip, Color(127, 127, 255)) #RED
                time.sleep(0.3)
                music("samples/elec_chime.wav")
                picture("images/adventure-time.png","Adventure Time!",580,326)
                time.sleep(duration)
            elif event.button == 7:
                print("CIRCLE")
                theaterChase(strip, Color(0, 255, 255)) #RED
                music("samples/perc_bell.wav")
                picture("images/unicorn.jpg","Unicorns!!",540,530)
                time.sleep(duration)
            elif event.button == 8:
                print("SELECT")
                time.sleep(duration)
            elif event.button == 9:
                print("START")
        elif event.type == pygame.QUIT:
            print("EXIT")
            pygame.quit()
