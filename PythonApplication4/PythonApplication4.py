import sys
import pygame
def run_game():
    pygame.init()
    screen=pygame.display.set_mode((800,800))#1200*800
    pygame.display.set_caption("alien !")
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
                pygame.display.filp()
run_game()
