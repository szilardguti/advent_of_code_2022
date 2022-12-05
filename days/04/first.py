def get_ids_from_start_to_end(start, end):
    result = []
    for i in range(int(start), int(end)+1):
        result.append(i)
    return result

with open('input.txt') as inp:
    lines = inp.read()
    lines = lines.split('\n')
    countOfResults = 0

    for line in lines:
        firstID, secondID = line.split(',')
        firstStart, firstEnd = firstID.split('-')
        secondStart, secondEnd = secondID.split('-')

        firstListOfIDs = get_ids_from_start_to_end(int(firstStart), int(firstEnd))
        secondListOfIDs = get_ids_from_start_to_end(int(secondStart), int(secondEnd))

        shorterList = []; longerList = [];
        if len(firstListOfIDs) < len(secondListOfIDs):
            shorterList = firstListOfIDs
            longerList = secondListOfIDs
        elif len(secondListOfIDs) < len(firstListOfIDs):
            shorterList = secondListOfIDs
            longerList = firstListOfIDs
        else:
            shorterList = firstListOfIDs
            longerList = secondListOfIDs

        elemFound = 0
        for elem in shorterList:
            if elem in longerList:
                elemFound = elemFound + 1

        if elemFound == len(shorterList):
            countOfResults = countOfResults + 1

    print(countOfResults)