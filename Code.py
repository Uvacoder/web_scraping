import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

                                      #Add Music
pygame.mixer.init()
pygame.mixer.music.load('Best Hacker music Deface Music EVER love khan.mp3')
pygame.mixer.music.play()
sleep(15)                             #Playing Music

pygame.mixer.music.stop()             #Stop Music
sleep(1)

                                      #Add New Music
pygame.mixer.music.load('Hacker.mp3')
pygame.mixer.music.play()
                                      #Add Picture
photo = pygame.image.load('Watch-Dogs-2-Widescreen-.jpg')

                                      #Update Screen
window.blit(photo, (0, 0))
pygame.display.update()
sleep(25)
