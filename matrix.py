"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    l1 = ''
    l2 = ''
    l3 = ''
    l4 = ''
    for coord in matrix:
        l1 += '{} '.format(coord[0])
        l2 += '{} '.format(coord[1])
        l3 += '{} '.format(coord[2])
        l4 += '{} '.format(coord[3])
    print(l1)
    print(l2)
    print(l3)
    print(l4)

a = [[2,2,3,4],[12,3,45,65],[433,4,5,2],[2,4,6,30]]
#print_matrix(a)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    r = 0
    while r < len(matrix):
        c = 0
        while c < len(matrix[r]):
            if r == c:
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0
            c += 1
        r += 1

#ident(a)
#print_matrix(a)

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    a = 0
    while a < len(m2):
        new = []
        b = 0
        while b < len(m2):
            s = 0
            c = 0
            while c < len(m1):
                s += m1[c][b] * m2[a][c]
                c += 1
            new.append(s)
            b += 1
        m2[a] = new
        a += 1
'''
a = [[4,8],[2,3],[4,1]]
b = [[3,2,7],[5,8,9]]
'''

a = [[-3,-3,-1,3,-5],[-1,-3,-5,2,3],[-1,-4,3,-1,-2],[-5,-5,-1,-4,-1],[1,3,-3,-4,-1]]
b = [[0,5,3,4,4],[5,5,0,0,-2],[3,2,-4,-3,0],[-3,0,-1,2,-1],[0,-1,-4,4,3]]
matrix_mult(a,b)
print(b)


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
