import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.mixer.init()
pygame.mixer.music.load('Powfu - dead eyes ft.Ouse.mp3')
pygame.mixer.music.play(start=15)
#pygame.mixer.music.play()
sleep(15)

pygame.mixer.music.stop()
sleep(5)


pygame.mixer.music.load('Rema - Fame (A COLORS ENCORE ).mp3')
pygame.mixer.music.play()

photo = pygame.image.load('1_vVsajU3uc1r3IPnXdIiCZA.jpg')
window.blit(photo, (0, 0))
pygame.display.update()
sleep(30)
