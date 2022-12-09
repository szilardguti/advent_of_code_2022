with open("input.txt", "r") as f:
    lines = f.read()
    lines = lines.split('\n')
    tree_matrix = []

    for line in lines:
        tree_matrix.append([ int(tree_height) for tree_height in line ])

    row_size = len(tree_matrix[0])
    col_size = len(tree_matrix)
    visible_tree_count = 0

    for row_index in range(row_size):
        for col_index in range(col_size):

            left_visible = True
            up_visible = True
            right_visible = True
            down_visible = True

            test_row = row_index
            test_col = col_index
            current_tree_size = tree_matrix[row_index][col_index]

            # LEFT visibility check
            while test_col != 0:
                test_col = test_col - 1
                test_tree_size = tree_matrix[test_row][test_col]

                if test_tree_size >= current_tree_size:
                    left_visible = False
                    break
            
            if left_visible:
                visible_tree_count = visible_tree_count + 1
                print('found left')
                continue

            test_row = row_index
            test_col = col_index
            # RIGHT visibility check
            while test_col != col_size-1:
                test_col = test_col + 1
                test_tree_size = tree_matrix[test_row][test_col]

                if test_tree_size >= current_tree_size:
                    right_visible = False
                    break
            
            if right_visible:
                visible_tree_count = visible_tree_count + 1
                print('found right')
                continue
            
            test_row = row_index
            test_col = col_index
            # UP visibility check
            while test_row != 0:
                test_row = test_row - 1
                test_tree_size = tree_matrix[test_row][test_col]
                
                if test_tree_size >= current_tree_size:
                    up_visible = False
                    break
            
            if up_visible:
                visible_tree_count = visible_tree_count + 1
                print('found up')
                continue
            
            test_row = row_index
            test_col = col_index
            # DOWN visibility check
            while test_row != row_size-1:
                test_row = test_row + 1
                test_tree_size = tree_matrix[test_row][test_col]

                if test_tree_size >= current_tree_size:
                    down_visible = False
                    break
            
            if down_visible:
                visible_tree_count = visible_tree_count + 1
                print('found down')
                continue

    print(visible_tree_count)