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

def char_running():
    pass

def set_direction():
    pass



#while (True):
for i in range(0,5):
        clear_canvas()
        h_x,h_y=hand_setting()
        back.draw(400, 300)
        hand.draw(h_x, h_y)
        update_canvas()
        delay(1)


close_canvas()