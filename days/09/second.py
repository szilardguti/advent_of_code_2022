def printMove(rope, direction, indx, only_stars = False):
    with open("output.txt", "a") as outp:
        rope_length = 1000
        print_map = [['.' for i in range(rope_length)] for j in range(rope_length)]
        reversed_rope = rope[::-1]

        i = len(rope)-1
        for knot in reversed_rope:
            if only_stars:
                print_map[knot[1]][knot[0]] = '*'
            else:
                print_map[knot[1]][knot[0]] = str(i)
                i = i - 1

        outp.write("{0} - {1}\n".format(direction, indx+1))
        for line in print_map:
            outp.write(''.join(line))
            outp.write('\n')
        outp.write('--' * 30)
        outp.write('\n')

POSSIBLE_MOVES = dict({(-2,-2) : (-1,-1), (-2,-1) : (-1,-1), (-2, 0) : (-1, 0), (-2, 1) : (-1, 1), (-2, 2) : (-1, 1),
                ( 2,-2) : ( 1,-1), ( 2,-1) : ( 1,-1), ( 2, 0) : ( 1, 0), ( 2, 1) : ( 1, 1), ( 2, 2) : ( 1, 1), 
                (-1, 2) : (-1, 1), ( 0, 2) : ( 0, 1), ( 1, 2) : ( 1, 1),
                (-1,-2) : (-1,-1), ( 0,-2) : ( 0,-1), ( 1,-2) : ( 1,-1)})

with open("input.txt", 'r') as f:
    open('output.txt', 'w').close()
    lines = f.read()
    lines = lines.split('\n')

    rope_knot_count = 10
    rope_knots = [ (50,50) for i in range(rope_knot_count)]

    tail_move_set = set()
    tail_move_set.add(rope_knots[-1])

    for line in lines:
        direction, move_count = line.split(' ')

        for i in range(int(move_count)):
            if direction == 'U':
                rope_knots[0] = (rope_knots[0][0], rope_knots[0][1]-1)
            if direction == 'D':
                rope_knots[0] = (rope_knots[0][0], rope_knots[0][1]+1)
            if direction == 'L':
                rope_knots[0] = (rope_knots[0][0]-1, rope_knots[0][1])
            if direction == 'R':
                rope_knots[0] = (rope_knots[0][0]+1, rope_knots[0][1])

            for j in range(1, rope_knot_count):

                move = POSSIBLE_MOVES.get((rope_knots[j-1][0] - rope_knots[j][0],rope_knots[j-1][1] - rope_knots[j][1]))
                if not move:
                    continue
                rope_knots[j] = (rope_knots[j][0] + move[0], rope_knots[j][1] + move[1]) 
                
                if j == rope_knot_count-1:
                    tail_move_set.add(rope_knots[j])
            
            # print('head: ', head, 'tail: ', tail)
        #printMove(rope_knots, direction, i)

    print(len(tail_move_set))
    printMove(list(tail_move_set), "result", len(tail_move_set), only_stars=True)