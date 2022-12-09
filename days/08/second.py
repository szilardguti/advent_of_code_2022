with open("input.txt", "r") as f:
    lines = f.read()
    lines = lines.split('\n')
    tree_matrix = []

    for line in lines:
        tree_matrix.append([ int(tree_height) for tree_height in line ])

    row_size = len(tree_matrix[0])
    col_size = len(tree_matrix)
    max_scenic_score = 0

    for row_index in range(row_size):
        for col_index in range(col_size):

            left_scenic_score = 0
            right_scenic_score = 0
            up_scenic_score = 0
            down_scenic_score = 0

            test_row = row_index
            test_col = col_index
            current_tree_size = tree_matrix[row_index][col_index]

            # LEFT visibility check
            while test_col != 0:
                left_scenic_score = left_scenic_score + 1
                test_col = test_col - 1
                test_tree_size = tree_matrix[test_row][test_col]

                if test_tree_size >= current_tree_size:
                    break


            test_row = row_index
            test_col = col_index
            # RIGHT visibility check
            while test_col != col_size-1:
                right_scenic_score = right_scenic_score + 1
                test_col = test_col + 1
                test_tree_size = tree_matrix[test_row][test_col]

                if test_tree_size >= current_tree_size:
                    break
            

            test_row = row_index
            test_col = col_index
            # UP visibility check
            while test_row != 0:
                up_scenic_score = up_scenic_score + 1
                test_row = test_row - 1
                test_tree_size = tree_matrix[test_row][test_col]
                
                if test_tree_size >= current_tree_size:
                    break
            

            test_row = row_index
            test_col = col_index
            # DOWN visibility check
            while test_row != row_size-1:
                down_scenic_score = down_scenic_score + 1
                test_row = test_row + 1
                test_tree_size = tree_matrix[test_row][test_col]

                if test_tree_size >= current_tree_size:
                    break
            
            current_scenic_score = left_scenic_score * right_scenic_score * down_scenic_score * up_scenic_score
            if current_scenic_score > max_scenic_score:
                max_scenic_score = current_scenic_score
                
    print(max_scenic_score)