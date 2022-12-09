from bigtree import Node, print_tree

root = Node("root", file_list=[])
currentNode = None
upNode = None
dir_dict = dict()

def sum_branch(branch_root):
    stack_sum = 0
    for file in branch_root.file_list:
        stack_sum = stack_sum + file[0]

    for child in branch_root.children:
        stack_sum = stack_sum + sum_branch(child)
    dir_dict.update({branch_root.path_name : stack_sum})
    return stack_sum

with open("input.txt", "r") as f:
    lines = f.read()
    lines = lines.split('\n')

    for line in lines:
        row = line.split(' ')
        if row[0] == '$':
            if row[1] == 'cd':
                if row[2] == '/':
                    currentNode = root
                    upNode = None
                    continue
                if row[2] == '..':
                    currentNode = currentNode.parent
                    upNode = currentNode.parent
                    continue
                else:
                    for child in currentNode.children:
                        if child.name == row[2]:
                            upNode = currentNode
                            currentNode = child
                            break
                    continue
            elif row[1] == 'ls':
                print('ls')

        elif row[0] == 'dir':
            if row[1] not in [child.name for child in currentNode.children ]:
                Node(row[1], parent=currentNode, file_list=[])

        elif row[0].isnumeric():
            currentNode.file_list.append((int(row[0]), row[1]))

print_tree(root, attr_list=["file_list"])
sum_branch(root)

result = 0
for key in dir_dict:
    value = dir_dict[key]
    if value <= 100000:
        result = result + value

print(result)