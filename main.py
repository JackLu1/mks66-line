from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
draw_line(0,0,500,10,screen,[255,255,255])
draw_line(0,0,250,50,screen,[255,255,255])
draw_line(100,100,250,159,screen,[255,255,255])
draw_line(00,100,250,159,screen,[255,255,255])
# for i in range(200):
#     plot(screen, color, i, i)
#     plot(screen, color, i, 20+i)

display(screen)
save_extension(screen, 'img.png')
