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

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    pass

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
