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
    for i in range(0, len(lines), 3):
        groupLine = lines[i] + lines[i+1] + lines[i+2]
        badgeSet = set()
        
        for currChar in groupLine:
            j1 = lines[i].find(currChar)
            j2 = lines[i+1].find(currChar)
            j3 = lines[i+2].find(currChar)

            if j1 != -1 and j2 != -1 and j3 != -1:
                badgeSet.add(currChar)
            
            groupLine.replace(currChar, '')
        sumOfPrio = sumOfPrio + get_priority(badgeSet)
    print(sumOfPrio)