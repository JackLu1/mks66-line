from display import *
from draw import *

import math

screen = new_screen()
color = [ 0, 0, 255 ]



i = 0
while i <= 500:
    draw_line(250,250,i,300,screen,color)
    draw_line(250,250,i,200,screen,color)
    draw_line(250,250,300,i,screen,color)
    draw_line(250,250,200,i,screen,color)
    i += 5

display(screen)
save_extension(screen, 'img.png')
