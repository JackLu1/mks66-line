from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -1 * (x1 - x0)
    while x <= x1:
        plot( screen, color, x, y )

