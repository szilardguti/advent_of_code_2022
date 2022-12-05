def get_priority(setOfChars):
    prios = []
    for currChar in setOfChars:
        if str(currChar).isupper() :
            prios.append(ord(currChar) - 65 + 27)
        else: 
            prios.append(ord(currChar) - 96)
            
    return sum(prios)

with open('input.txt') as inp:
    lines = inp.read()
    lines = lines.split('\n')

    sumOfPrio = 0
    for line in lines:
        halfPoint = int(len(line)/2)

        firstRuck = line[:halfPoint]
        secondRuck = line[halfPoint:]

        currFoundLetters = set()
        for currChar in firstRuck:
            res = secondRuck.find(currChar)
            if res != -1:
                currFoundLetters.add(currChar)
        
        sumOfPrio = sumOfPrio + get_priority(currFoundLetters)

    print(sumOfPrio)