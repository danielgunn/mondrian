import pygame
from pygame.math import Vector2
from random import randint

colors = [(0xff,0xff,0xff),(0xfa, 0xc9, 0x01),(0x22, 0x50, 0x95),(0xdd,0x01,0x00)]
width = 300
height = 400

min_rectangle_width = int(0.3 * width)
min_rectangle_height = int(0.3 * height)

def draw_mondrian(screen, tl, br):
    c = colors[randint(0, len(colors)-1)]
    screen.fill(c, pygame.Rect(tl, br))
    pygame.draw.rect(screen,(0,0,0), pygame.Rect(tl, br), 10)
    can_split_y = (tl[1] + min_rectangle_height) < 0.8 * br[1]
    can_split_x = (tl[0] + min_rectangle_width) < 0.8 * br[0]
    if can_split_x and can_split_y:
        if randint(0,1) == 0:
            y_split = randint((tl[1] + min_rectangle_height), int(0.8 * br[1]))
            draw_mondrian(screen, tl, Vector2(br[0],y_split))
            draw_mondrian(screen, Vector2(tl[0],y_split),br)
        else :
            x_split= randint((tl[0] + min_rectangle_width), int(0.8 * br[0]))
            draw_mondrian(screen, tl, Vector2(x_split, br[1]))
            draw_mondrian(screen, Vector2(x_split, tl[1]), br)
    elif can_split_x:
        x_split = randint((tl[0] + min_rectangle_width), int(0.8 * br[0]))
        draw_mondrian(screen, tl, Vector2(x_split, br[1]))
        draw_mondrian(screen, Vector2(x_split, tl[1]), br)
    elif can_split_y:
        y_split = randint((tl[1] + min_rectangle_height), int(0.8 * br[1]))
        draw_mondrian(screen, tl, Vector2(br[0], y_split))
        draw_mondrian(screen, Vector2(tl[0], y_split), br)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mondrian -- press space for another")

draw_mondrian(screen, Vector2(0,0), Vector2(screen.get_width(), screen.get_height()))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                draw_mondrian(screen, Vector2(0, 0), Vector2(screen.get_width(), screen.get_height()))

    pygame.display.flip()