import sys
import pygame as pg

pg.init()
size = 800,600
ekran = pg.display.set_mode(size)
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            sys.exit()
    ekran.fill((0,255,0))
    pg.display.flip()
    