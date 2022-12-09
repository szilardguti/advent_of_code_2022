with open("input.txt", 'r') as f:
    lines = f.read()
    lines = lines.split('\n')

    head = (0,0)
    tail = (0,0)

    tail_move_set = set()

    for line in lines:
        direction, move_count = line.split(' ')

        for i in range(int(move_count)):
            if direction == 'U':
                head = (head[0], head[1]+1)
            if direction == 'D':
                head = (head[0], head[1]-1)
            if direction == 'L':
                head = (head[0]-1, head[1])
            if direction == 'R':
                head = (head[0]+1, head[1])

            x_distance = abs(head[0] - tail[0])
            y_distance = abs(head[1] - tail[1])

            if x_distance == 2 and y_distance == 0 or x_distance == 2 and y_distance == 1:
                if direction == 'R':
                    tail = (head[0]-1, head[1])
                if direction == 'L':
                    tail = (head[0]+1, head[1])

            if x_distance == 0 and y_distance == 2 or x_distance == 1 and y_distance == 2:
                if direction == 'U':
                    tail = (head[0], head[1]-1)
                if direction == 'D':
                    tail = (head[0], head[1]+1)

            tail_move_set.add(tail)
            
            # print('head: ', head, 'tail: ', tail)

    print(len(tail_move_set))