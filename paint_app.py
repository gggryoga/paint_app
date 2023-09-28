import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))
drawing = False
last_pos = None
line_color = pg.Color('red')
line_width = 5
screen.fill(pg.Color('white'))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左クリックが押された場合
                drawing = True
                last_pos = event.pos
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:  # 左クリックが離された場合
                drawing = False
                last_pos = None

    if drawing:
        current_pos = pg.mouse.get_pos()
        if last_pos is not None:
            pg.draw.line(screen, line_color, last_pos, current_pos, line_width)
        last_pos = current_pos

    # 画面の更新
    pg.display.update()

    if pg.key.get_pressed()[pg.K_ESCAPE]:
        pg.quit()
        sys.exit()

    pg.time.Clock().tick(60)
