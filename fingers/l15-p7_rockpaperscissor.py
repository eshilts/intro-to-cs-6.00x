import random
import pylab

def gamePlay(player1, player2):
    if player1 == player2:
        return 'Push'
    elif player1 == 'paper':
        if player2 == 'rock':
            return True
        return False
    elif player1 == 'rock':
        if player2 == 'scissor':
            return True
        return False
    elif player1 == 'scissor':
        if player2 == 'paper':
            return True
        return False
    else:
        raise "Wrong arguments"

def generateWins(numRounds = 10):
    wins = 0.0
    
    for round in range(numRounds):
        while True:
            player1 = 'rock'
            player2 = random.choice(['rock', 'paper', 'scissor'])
            result = gamePlay(player1, player2)

            if result == 'Push':
                next
            elif result:
                wins += 1

            break

    return wins

def simulateGame(numRounds = 10, numTrials = 100):
    winsEachTrial = []

    for trial in range(numTrials):
        winsEachTrial.append(generateWins(numRounds) / numRounds)

    return winsEachTrial

def produceHistogram(proportions):
    meanProportion = sum(proportions) / len(proportions)

    print "Proportions {0} - {1}".format(proportions[:10], proportions[-10:])
    pylab.figure(1)
    pylab.hist(proportions, bins=11)
    
    ymin, ymax = pylab.ylim()
    xmin, xmax = pylab.xlim()
    ymid = (ymax - ymin) / 2
    pylab.text(xmin + (xmax - xmin) * 0.02, ymid, "Win proportion\nMean = {0}".format(
        str(round(meanProportion, 3))))

    pylab.title("Rock-Paper-Scissor: Rock Only Wins vs A Random Player")
    pylab.xlabel("Proportion of Wins from Only Choosing Rock")
    pylab.ylabel("Number of Games")
    pylab.show()

produceHistogram(simulateGame(50, 1000))
