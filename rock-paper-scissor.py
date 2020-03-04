from random import randint as getRandom

def getUserMove():
    print('Moves:\n1. Rock\n2. Paper\n3. Scissor')
    userMove = input('Pick Rock, Paper, or Scissors (1, 2, or 3):')
    return int(userMove)

def getComputerMove():
    return getRandom(1,3)

# returns 'COM', 'USER', or 'TIE', based on the moves of the user and computer
def getWinner(userMove, comMove):
    if userMove == 1:
        if comMove == 1:
            return 'TIE'
        elif comMove == 2:
            return 'COM'
        else:
            return 'USER'
    elif userMove == 2:
        if comMove == 1:
            return 'USER'
        elif comMove == 2:
            return 'TIE'
        else:
            return 'COM'
    else:
        if comMove == 1:
            return 'COM'
        elif comMove == 2:
            return 'USER'
        else:
            return 'TIE'

def updateScore(winner, score):
    if winner == 'USER':
        return [score[0]+1, score[1]]
    elif winner == 'COM':
        return [score[0], score[1]+1]
    else:
        return score

def displayScore(winner, score):
    if winner !='TIE':
        print(winner,'won!')
        print('USER:', score[0],'\tCOM:',score[1])
    else:
        print('Tie game!')
        print('USER:', score[0],'\tCOM:',score[1])

if __name__ == "__main__":
    score = [0,0]

    play = 'y'

    while play != 'n':
        userMove = getUserMove()
        comMove = getComputerMove()
        winner = getWinner(userMove, comMove)
        score = updateScore(winner, score)

        displayScore(winner,score)
        
        play = input('Would you like to play again (y/n)?:')