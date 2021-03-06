import sys
import pygame as pg

pg.init()
size = width, height = 800, 600
speed = [1, 1]
black = 0, 0, 0
screen = pg.display.set_mode(size)
ball = pg.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(ball, ballrect)
    pg.display.flip()
