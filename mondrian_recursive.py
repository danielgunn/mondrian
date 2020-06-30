import pygame
from pygame.math import Vector2
from random import randint

colors = [(0xff,0xff,0xff),(0xfa, 0xc9, 0x01),(0x22, 0x50, 0x95),(0xdd,0x01,0x00)]
width = 612
height = 1024

min_rectangle_width = int(0.3 * width)
min_rectangle_height = int(0.3 * height)

def draw_mondrian(screen, top_left=Vector2(0,0), bottom_right=Vector2(width,height)):
    c = colors[randint(0, len(colors)-1)]
    screen.fill(c, pygame.Rect(top_left, bottom_right))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(top_left, bottom_right), 10)
    can_split_y = (top_left[1] + min_rectangle_height) < 0.8 * bottom_right[1]
    can_split_x = (top_left[0] + min_rectangle_width) < 0.8 * bottom_right[0]
    if can_split_x and can_split_y:
        if randint(0,1) == 0:
            y_split = randint((top_left[1] + min_rectangle_height), int(0.8 * bottom_right[1]))
            draw_mondrian(screen, top_left, Vector2(bottom_right[0], y_split))
            draw_mondrian(screen, Vector2(top_left[0], y_split), bottom_right)
        else :
            x_split= randint((top_left[0] + min_rectangle_width), int(0.8 * bottom_right[0]))
            draw_mondrian(screen, top_left, Vector2(x_split, bottom_right[1]))
            draw_mondrian(screen, Vector2(x_split, top_left[1]), bottom_right)
    elif can_split_x:
        x_split = randint((top_left[0] + min_rectangle_width), int(0.8 * bottom_right[0]))
        draw_mondrian(screen, top_left, Vector2(x_split, bottom_right[1]))
        draw_mondrian(screen, Vector2(x_split, top_left[1]), bottom_right)
    elif can_split_y:
        y_split = randint((top_left[1] + min_rectangle_height), int(0.8 * bottom_right[1]))
        draw_mondrian(screen, top_left, Vector2(bottom_right[0], y_split))
        draw_mondrian(screen, Vector2(top_left[0], y_split), bottom_right)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mondrian -- press space for another")

draw_mondrian(screen)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                draw_mondrian(screen)

    pygame.display.flip()