from display import *
from draw import *
from iparser import *
from matrix import *
import sys

screen = new_screen()
color = [ 0, 255, 0 ]
stack = [ident(new_matrix())]

if len(sys.argv) == 2:
    f = open(sys.argv[1])

parse_file( f, stack, screen, color )
f.close()
