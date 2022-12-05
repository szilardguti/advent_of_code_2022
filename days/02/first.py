with open('input.txt') as inp:
    lines = inp.read()
    lines = lines.split('\n')

# X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won

    pointDictionary = {
        "A" : {
            "X" : 4,
            "Y" : 8,
            "Z" : 3
        },
        "B" : {
            "X" : 1,
            "Y" : 5,
            "Z" : 9
        },
        "C" : {
            "X" : 7,
            "Y" : 2,
            "Z" : 6
        }
    }

    sumScore = 0
    for line in lines:
        enemyAns, myAns = line.split(' ')
        sumScore = sumScore + pointDictionary[enemyAns][myAns]

    print(sumScore)
        