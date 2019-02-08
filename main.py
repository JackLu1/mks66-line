from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
i = 250
while i < 500:
    draw_line(250,250,500,i,screen,[255,255,255])
    i += 10
draw_line(250,250,500,0,screen,[255,255,255])
#draw_line(250,250,500,350,screen,[255,255,255])
#draw_line(250,250,500,250,screen,[255,255,255])
#draw_line(250,250,500,-100,screen,[255,255,255])

#draw_line(0,0,250,50,screen,[255,255,255])
#draw_line(100,100,250,159,screen,[0,0,255])
#draw_line(00,100,250,159,screen,[0,255,0])
# for i in range(200):
#     plot(screen, color, i, i)
#     plot(screen, color, i, 20+i)

display(screen)
save_extension(screen, 'img.png')
