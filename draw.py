from display import *

def line(x, y):
    return 2 * x + y

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -1 * (x1 - x0)
    dy = y1 - y0
    dx = x1 - x0

    # oct 1
    if dy >= 0 and dx >= 0 and dy <= dx:
        d = line(A, B)
        while x <= x1:
            plot( screen, color, x, y )
            if d > 0:
                y += 1
                d += 2*B
            x += 1
            d += 2*A

    # oct 2
    if dy >= 0 and dx >= 0 and dy >= dx:
        d = line(B, A)
        while y <= y1:
            plot( screen, color, x, y )
            if d < 0:
                x += 1
                d += 2*A
            y += 1
            d += 2*B

    # oct 3
    if dy >= 0 and dx <= 0 and dy >= abs(dx):
        B = x1 - x0
        d = line(B, A)
        while y <= y1:
            plot( screen, color, x, y )
            if d < 0:
                x -= 1
                d += 2*A
            y += 1
            d += 2*B
    # oct 4
    if dy >= 0 and dx <= 0 and dy <= abs(dx):
        B = x1 - x0
        d = line(A, B)
        while x >= x1:
            plot( screen, color, x, y )
            if d > 0:
                y += 1
                d += 2*B
            x -= 1
            d += 2*A
    # oct 5
    if dy <= 0 and dx <= 0 and abs(dy) <= abs(dx):
        A = y0 - y1
        B = x1 - x0
        d = line(A, B)
        while x >= x1:
            plot( screen, color, x, y )
            if d > 0:
                y -= 1
                d += 2*B
            x -= 1
            d += 2*A
    # oct 6
    if dy <= 0 and dx <= 0 and abs(dy) >= abs(dx):
        A = y1 - y0
        B = x1 - x0
        d = line(B, -1*A)
        while y >= y1:
            plot( screen, color, x, y )
            if d < 0:
                x -= 1
                d -= 2*A
            y -= 1
            d += 2*B
    # oct 7
    if dy <= 0 and dx >= 0 and abs(dy) >= abs(dx):
        d = line(B, -1*A)
        while y >= y1:
            plot( screen, color, x, y )
            if d < 0:
                x += 1
                d -= 2*A
            y -= 1
            d += 2*B
    # oct 8
    if dy <= 0 and dx >= 0 and abs(dy) <= abs(dx):
        A = y0 - y1
        B = -1 * (x1 - x0)
        d = line(A, B)
        while x <= x1:
            plot( screen, color, x, y )
            if d > 0:
                y -= 1
                d += 2*B
            x += 1
            d += 2*A

