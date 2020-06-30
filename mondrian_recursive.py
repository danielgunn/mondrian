import pygame
from pygame.math import Vector2
from random import randint

colors = [(0xff,0xff,0xff),(0xfa, 0xc9, 0x01),(0x22, 0x50, 0x95),(0xdd,0x01,0x00)]
width = 612
height = 1024
min_scaling_factor = 0.8

def draw_mondrian(
        screen,
        min_rectangle_width = int(0.3 * width),
        min_rectangle_height = int(0.3 * height),
        top_left=Vector2(0,0),
        bottom_right=Vector2(width,height)):

    # draw this rectangle
    c = colors[randint(0, len(colors)-1)]
    screen.fill(c, pygame.Rect(top_left, bottom_right))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(top_left, bottom_right), 10)

    max_rectangle_width = int(min_scaling_factor * (bottom_right[0] - top_left[0]))
    max_rectangle_height = int(min_scaling_factor * (bottom_right[1] - top_left[1]))

    can_split_x = 2*min_rectangle_width < max_rectangle_width
    can_split_y = 2*min_rectangle_height < max_rectangle_height

    if not(can_split_x or can_split_y):
        return

    if can_split_x:
        x_split = top_left[0] + randint(min_rectangle_width, max_rectangle_width - min_rectangle_width)

    if can_split_y:
        y_split = top_left[1] + randint(min_rectangle_height, max_rectangle_height - min_rectangle_height)

    if can_split_x and can_split_y:
        if randint(0,1) == 0:
            draw_mondrian(screen, min_rectangle_width, min_rectangle_height, top_left, Vector2(bottom_right[0], y_split))
            draw_mondrian(screen, min_rectangle_width, min_rectangle_height, Vector2(top_left[0], y_split), bottom_right)
        else :
            draw_mondrian(screen, min_rectangle_width, min_rectangle_height, top_left, Vector2(x_split, bottom_right[1]))
            draw_mondrian(screen, min_rectangle_width, min_rectangle_height, Vector2(x_split, top_left[1]), bottom_right)
    elif can_split_x:
        draw_mondrian(screen, min_rectangle_width, min_rectangle_height, top_left, Vector2(x_split, bottom_right[1]))
        draw_mondrian(screen, min_rectangle_width, min_rectangle_height, Vector2(x_split, top_left[1]), bottom_right)
    elif can_split_y:
        draw_mondrian(screen, min_rectangle_width, min_rectangle_height, top_left, Vector2(bottom_right[0], y_split))
        draw_mondrian(screen, min_rectangle_width, min_rectangle_height, Vector2(top_left[0], y_split), bottom_right)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mondrian")

draw_mondrian(screen)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            draw_mondrian(screen, mousePos[0], mousePos[1])

    pygame.display.flip()