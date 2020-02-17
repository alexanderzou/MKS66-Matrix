from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 255 ]
matrix = new_matrix()

#adds edges of entire box and details inside
def draw_box(mat,x,y,t):
    add_edge(mat,x+10,y+10,0,x+10,y-10,0)
    add_edge(mat,x+10,y-10,0,x-10,y-10,0)
    add_edge(mat,x-10,y-10,0,x-10,y+10,0)
    add_edge(mat,x-10,y+10,0,x+10,y+10,0)
    if t == 'pl': #plain
        pass
    if t == 'bb': #big box
        add_edge(mat,x+8,y+8,0,x+8,y-8,0)
        add_edge(mat,x+8,y-8,0,x-8,y-8,0)
        add_edge(mat,x-8,y-8,0,x-8,y+8,0)
        add_edge(mat,x-8,y+8,0,x+8,y+8,0)
    if t == 'sb': #small box
        add_edge(mat,x+3,y+3,0,x+3,y-3,0)
        add_edge(mat,x+3,y-3,0,x-3,y-3,0)
        add_edge(mat,x-3,y-3,0,x-3,y+3,0)
        add_edge(mat,x-3,y+3,0,x+3,y+3,0)
    if t == 'br': #brick
        add_edge(mat,x-10,y+4,0,x+10,y+4,0)
        add_edge(mat,x-10,y-4,0,x+10,y-4,0)
        add_edge(mat,x-2,y+10,0,x-2,y+4,0)
        add_edge(mat,x-5,y+4,0,x-5,y-4,0)
        add_edge(mat,x+7,y+4,0,x+7,y-4,0)
        add_edge(mat,x+1,y-4,0,x+1,y-10,0)
    if t == 'w': #wood
        add_edge(mat,x-5,y+8,0,x-5,y+5,0)
        add_edge(mat,x+4,y+7,0,x+4,y+4,0)
        add_edge(mat,x,y,0,x,y+4,0)
        add_edge(mat,x-5,y,0,x-5,y-3,0)
        add_edge(mat,x-3,y-6,0,x-3,y-9,0)
        add_edge(mat,x+7,y-4,0,x+7,y-7,0)
    if t == 'sp': #spiral
        add_edge(mat,x-5,y-5,0,x+5,y-5,0)
        add_edge(mat,x+5,y-5,0,x+5,y+5,0)
        add_edge(mat,x+5,y+5,0,x-5,y+5,0)
        add_edge(mat,x-5,y+5,0,x-5,y-1,0)
        add_edge(mat,x-5,y-1,0,x,y-1,0)
        add_edge(mat,x,y-1,0,x,y+2,0)
    if t == 'c': #crate
        add_edge(mat,x-10,y+10,0,x+10,y-10,0)
        add_edge(mat,x+10,y+10,0,x-10,y-10,0)

matrix[0] = [0,0,0,1]
matrix[1] = [0,500,0,1]
matrix[2] = [500,0,0,1]
matrix[3] = [500,500,0,1]
pattern = [['br','br','bb','bb','sb','sb','sp','bb','bb','bb','sb','sb','sb','bb','bb','e','w','bb','w','w','w','w','sb','sb','sb'],\
           ['br','br','bb','sb','sb','sb','sp','sp','c','bb','sb','br','br','bb','w','e','w','bb','bb','bb','br','br','sb','sp','sp'],\
           ['pl','pl','bb','w','sb','sb','sp','sp','c','c','pl','br','br','bb','w','e','w','sp','pl','pl','br','br','sp','sp','c'],\
           ['c','pl','pl','w','sb','pl','sp','sp','c','pl','pl','pl','br','br','w','e','w','sp','sp','pl','pl','br','br','c','c'],\
           ['c','c','pl','w','pl','pl','sb','sp','c','pl','pl','pl','br','br','w','e','bb','bb','sp','sp','sp','br','br','sb','c'],\
           ['c','pl','pl','w','pl','w','sb','c','c','c','pl','w','w','w','w','e','bb','c','sp','sp','bb','sb','sb','sb','pl'],\
           ['c','pl','w','bb','bb','w','sb','sb','bb','bb','sb','sb','sb','e','e','e','bb','c','c','pl','bb','bb','bb','pl','pl'],\
           ['br','br','w','bb','bb','w','e','e','bb','e','sb','e','e','e','e','e','e','c','pl','pl','sb','sb','sb','pl','c'],\
           ['br','br','w','bb','bb','w','e','e','bb','e','e','e','e','e','e','e','e','e','pl','e','sb','br','br','c','c'],\
           ['c','c','w','bb','bb','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','br','br','e','c'],\
           ['c','pl','w','br','br'],\
           ['pl','pl','w','br','br'],\
           ['pl','e','w','br','br'],\
           ['sp','e','w','br','br'],\
           ['sp'],\
           [],[],[],[],\
           ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','w'],\
           ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','w'],\
           ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','w'],\
           ['e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','w']]
c = 10
i1 = 0
while i1 < len(pattern):
    r = 10
    i2 = 0
    while i2 < len(pattern[i1]):
        if pattern[i1][i2] != 'e':
            draw_box(matrix,r,c,pattern[i1][i2])
        r += 20
        i2 += 1
    c += 20
    i1 += 1
    

draw_lines( matrix, screen, color )
display(screen)
save_ppm_ascii(screen,'img.ppm')