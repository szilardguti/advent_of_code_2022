with open('input.txt') as inp:
    lines = inp.read()
    lines = lines.split('\n')

    maxCal = 0
    currCal = 0
    topThreeCal = [0, 0, 0]

    for line in lines:
        if line == '':

            for item in topThreeCal:
                if currCal > item:
                    topThreeCal.sort(reverse = True)
                    topThreeCal.pop()
                    topThreeCal.append(currCal)
                    break
                
            currCal = 0
        else:
            currCal = currCal + int(line)

    print(topThreeCal)
    print(sum(topThreeCal))
