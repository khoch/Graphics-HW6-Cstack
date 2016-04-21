from display import *
from matrix import *
from draw import *
import copy

ARG_COMMANDS = [ 'line', 'scale', 'translate', 'xrotate', 'yrotate', 'zrotate', 'circle', 'bezier', 'hermite', 'sphere', 'box', 'torus']

def parse_file( f, stack, screen, color ):

    commands = f.readlines()

    c = 0
    while c  <  len(commands):
        temp = []
        cmd = commands[c].strip()
        if cmd in ARG_COMMANDS:
            c+= 1
            args = commands[c].strip().split(' ')
            i = 0
            while i < len( args ):
                args[i] = float( args[i] )
                i+= 1

            if cmd == 'line':
                add_edge( temp, args[0], args[1], args[2], args[3], args[4], args[5] )
                matrix_mult( temp, stack[-1] )
                draw_lines( temp, screen, color )
                
            elif cmd == 'circle':
                add_circle( temp, args[0], args[1], 0, args[2], .01 )
                matrix_mult( temp, stack[-1] )
                draw_lines( temp, screen, color )
            
            elif cmd == 'bezier':
                add_curve( temp, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'bezier' )
                matrix_mult( temp, stack[-1] )
                draw_lines( temp, screen, color )
            
            elif cmd == 'hermite':
                add_curve( temp, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'hermite' )
                matrix_mult( temp, stack[-1] )
                draw_lines( temp, screen, color )

            elif cmd == 'sphere':
                add_sphere( temp, args[0], args[1], 0, args[2], 5 )
                matrix_mult( temp, stack[-1] )
                draw_polygons( temp, screen, color )

            elif cmd == 'torus':
                add_torus( temp, args[0], args[1], 0, args[2], args[3], 5 )
                matrix_mult( temp, stack[-1] )
                draw_polygons( temp, screen, color )

            elif cmd == 'box':
                add_box( temp, args[0], args[1], args[2], args[3], args[4], args[5] )
                matrix_mult( temp, stack[-1] )
                draw_polygons( temp, screen, color )


            elif cmd == 'scale':
                s = make_scale( args[0], args[1], args[2] )
                matrix_mult( s, stack[-1] )

            elif cmd == 'translate':
                t = make_translate( args[0], args[1], args[2] )
                matrix_mult( t, stack[-1] )

            else:
                angle = args[0] * ( math.pi / 180 )
                if cmd == 'xrotate':
                    r = make_rotX( angle )
                elif cmd == 'yrotate':
                    r = make_rotY( angle )
                elif cmd == 'zrotate':
                    r = make_rotZ( angle )
                matrix_mult( r, stack[-1] )

        elif cmd == 'push':
            stack.append(copy.deepcopy(stack[-1]))
            
        elif cmd == 'pop':
            stack.pop()
            
        elif cmd == 'ident':
            ident( transform )

        elif cmd in ['display', 'save' ]:
            if cmd == 'display':
                display( screen )

            elif cmd == 'save':
                c+= 1
                save_extension( screen, commands[c].strip() )
        
        elif cmd == 'quit':
            return    
        elif cmd[0] != '#':
            print 'Invalid command: ' + cmd
        c+= 1
