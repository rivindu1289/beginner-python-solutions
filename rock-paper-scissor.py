# Author: Rivindu Wijedoru (rivindu1289)
# Rock Paper Scissors program

from random import randint as getRandom

# gets what move the user selects:
# - 1 = Rock
# - 2 = Paper
# - 3 = Scissor
def getUserMove():
    print('\n\nclearMoves:\n1. Rock\n2. Paper\n3. Scissor')
    while True:
        userMove = input('Pick Rock, Paper, or Scissors (1, 2, or 3):')
        if userMove == '1' or userMove == '2' or userMove == '3':
            break
        print('Invalid input, try again')
    return int(userMove)

# gets a random move from the computer
def getComputerMove():
    return getRandom(1,3)

# returns 'COM' or 'USER' as the winner, or 'TIE' if there's a tie, based on the moves of the user and computer
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

# increments the winner's score by 1, does nothing if there is a tie
def updateScore(winner, score):
    if winner == 'USER':
        return [score[0]+1, score[1]]
    elif winner == 'COM':
        return [score[0], score[1]+1]
    else:
        return score

# returns the Move represented by the move number
def getMove(moveNum):
    moves = {
        1: "Rock",
        2: "Paper",
        3: "Scissor"
    }
    return moves.get(moveNum)

# displays the moves of the user and computer, who won, and the score
def displayResults(userMove, comMove, winner, score):
    print("\nUSER:", getMove(userMove), "\tCOM:", getMove(comMove))

    if winner !='TIE':
        if winner == 'USER':
            print(getMove(userMove), 'beats', getMove(comMove))
        else:
            print(getMove(comMove), 'beats', getMove(userMove))
        print(winner,'won!')
        print('USER:', score[0],'\tCOM:',score[1])
    else:
        print('Tie game!')
        print('USER:', score[0],'\tCOM:',score[1])

# main function
if __name__ == "__main__":
    score = [0,0]

    play = 'y'

    while play != 'n': # loop to play as many times as the user likes
        userMove = getUserMove()
        comMove = getComputerMove()
        winner = getWinner(userMove, comMove)
        score = updateScore(winner, score)

        displayResults(userMove, comMove, winner, score)
        
        play = input('Would you like to play again (y/n)?:')