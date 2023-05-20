import pygame
from pygame import mixer

pygame.mixer.init()

mixer.music.load("Mario Sound.mp3")

mixer.music.set_volume(0.9)

mixer.music.play(-1) #sürekli loop da kalmasını sağlıyor.

soundeffect = pygame.mixer.Sound("Coin Sound.mp3")

while True:

    print("press 1.pause, 2.play, 3.resume, 4.stop, 5.add effect, 6.quit")
    a = input("  ")

    if a == "1":
        mixer.music.pause()

    elif a == "2":
        mixer.music.play(0)

    elif a == "3":
        mixer.music.unpause()

    elif a == "4":
        mixer.music.pause()
    
    elif a == "5":
        soundeffect.play()
    
    elif a == "6":

        pygame.quit()
        quit()
        break
