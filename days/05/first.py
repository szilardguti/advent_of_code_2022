with open("input.txt", "r") as f:
    lines = f.read()
    lines = lines.split('\n')

    startingPosData = [ item for item in lines[0:lines.index('')]]
    moves = [ moveLine for moveLine in lines[lines.index('')+1:]]

    numberOfStacks = max([ int(num) for num in startingPosData.pop().split(' ') if num != ''])

    listOfStacks = list()
    for i in range(numberOfStacks):
        listOfStacks.append(list())

    startingPosData.reverse()
    for stackItems in startingPosData:
        j = 0
        for i in range(1, 1+4*numberOfStacks, 4):
            if stackItems[i] != ' ':
                listOfStacks[j].append(stackItems[i])
            j = j + 1

    print("input processing done: ")
    print(listOfStacks)

    for move in moves:
        moveCount = int(move.split()[1])
        moveFrom = int(move.split()[3])-1
        moveTo = int(move.split()[5])-1

        for elemCount in range(moveCount):
            listOfStacks[moveTo].append(listOfStacks[moveFrom].pop())

    resultString = ""
    for crateStack in listOfStacks:
        resultString = resultString + crateStack.pop()

    print(resultString)