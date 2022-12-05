with open('input.txt') as inp:
    lines = inp.read()
    lines = lines.split('\n')

#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
# X for Rock, Y for Paper, and Z for Scissors

    resultDictionary = {
        "A" : {
            "X" : "Z",
            "Y" : "X",
            "Z" : "Y"
        },
        "B" : {
            "X" : "X",
            "Y" : "Y",
            "Z" : "Z"
        },
        "C" : {
            "X" : "Y",
            "Y" : "Z",
            "Z" : "X"
        }
    }

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
        enemyAns, res = line.split(' ')
        myAns = resultDictionary[enemyAns][res]
        sumScore = sumScore + pointDictionary[enemyAns][myAns]

    print(sumScore)
        