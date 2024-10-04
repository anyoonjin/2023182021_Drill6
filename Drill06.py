from pico2d import *
import random

open_canvas()
cha = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
back = load_image('TUK_GROUND.png')

def hand_setting():
    h_x=random.randint(0,760)
    h_y=random.randint(0,560)
    return h_x,h_y

def char_running(p1,p2):

    x1, y1 = p1
    x2, y2 = p2
    if x1==x2:
        return None,None
    a = (y2 - y1) / (x2 - x1)
    b = y1 - x1 * a
    return a,b


def set_direction():
    pass


p1=[400, 300]
frame=0
while (True):
    h_x,h_y=hand_setting()
    p2 = [h_x, h_y]

    a,b=char_running(p1, p2)

    if (p1[0] > p2[0]):
        dir=' '
        move_s = -10
    elif (p1[0] < p2[0]):
        dir='h'
        move_s = 10
    if a is not None:
        for x in range(p1[0], p2[0] + move_s , move_s):
            clear_canvas()
            back.draw(400, 300)
            hand.draw(h_x, h_y)
            y = a * x + b
            cha.clip_composite_draw(frame*100, 0, 100, 100,0,dir, x, y,100,100)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)
    else:
        if p1[1] > p2[1]:
            move_s = -5
        elif p1[1] < p2[1]:
            move_s = 5
        else:
            move_s = 0

        for y in range(p1[1], p2[1] + move_s, move_s):
            clear_canvas()
            back.draw(400, 300)
            hand.draw(h_x, h_y)
            cha.clip_composite_draw(frame*100, 0, 100, 100,0,dir, p1[0], y,100,100)  # x는 고정, y만 이동
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)

    p1=[p2[0],p2[1]]


close_canvas()