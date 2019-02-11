from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#i = 0
#while i < 250:
#    draw_oct3(250,250,i,500,screen,[255,255,255])
#    i += 25

# oct 3
draw_line(250,250,150,500,screen,color)
# oct 4
draw_line(250,250,0,500,screen,color)
draw_line(250,250,0,270,screen,color)

# oct 1
draw_line(250,250,500,250,screen,color)
draw_line(250,250,500,500,screen,color)

# oct 2
draw_line(250,250,300,500,screen,[255,255,255])
draw_line(250,250,359,500,screen,[255,255,255])
draw_line(250,250,250,500,screen,[255,255,255])

# oct 3
#draw_oct3(250,250,200,500,screen,color)
#draw_oct3(250,250,250,500,screen,color)
#draw_oct3(250,250,0,500,screen,color)

# oct 4
#draw_oct4(250,250,0,300,screen,color)
#draw_oct4(250,250,0,500,screen,color)
#draw_oct4(250,250,0,250,screen,color)

# oct 5
#draw_oct5(250,250,0,200,screen,color)
#draw_oct5(250,250,0,0,screen,color)
#draw_oct5(250,250,0,250,screen,color)

# oct 6
#draw_oct6(250,250,0,0,screen,color)
#draw_oct6(250,250,250,0,screen,color)
#draw_oct6(250,250,100,0,screen,color)

# oct 7
#draw_oct7(250,250,300,0,screen,color)
#draw_oct7(250,250,400,0,screen,color)
#draw_oct7(250,250,250,0,screen,color)

# oct 8
#draw_oct8(250,250,500,200,screen,color)
#draw_oct8(250,250,500,250,screen,color)
#draw_oct8(250,250,500,0,screen,color)
#draw_oct8(250,250,500,125,screen,color)


display(screen)
save_extension(screen, 'img.png')
