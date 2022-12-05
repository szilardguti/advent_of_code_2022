with open('input.txt') as inp:
    lines = inp.read()
    lines = lines.split('\n')

    maxCal = 0
    currCal = 0
    for line in lines:
        if line == '':
            if currCal > maxCal:
                maxCal = currCal
            currCal = 0
        else:
            currCal = currCal + int(line)

    print(maxCal)