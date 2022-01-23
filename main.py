import random

def checkInput(player):
    validInputs = ['0', '1', '2', 'r', 'p', 's', 'rock', 'paper', 'scissors']
    return player in validInputs


def compare(computer, player):
    if player == '0' or player == 'r' or player == 'rock':
        if computer == 0:
            print('You chose rock, computer chose rock')
            return 1
        elif computer == 1:
            print('You chose rock, computer chose paper')
            return 0
        else:
            print('You chose rock, computer chose scissors')
            return 2

    elif player == '1' or player == 'p' or player == 'paper':
        if computer == 0:
            print('You chose paper, computer chose rock')
            return 2
        elif computer == 1:
            print('You chose paper, computer chose paper')
            return 1
        else:
            print('You chose paper, computer chose scissors')
            return 0

    else:
        if computer == 0:
            print('You chose scissors, computer chose rock')
            return 0
        elif computer == 1:
            print('You chose scissors, computer chose paper')
            return 2
        else:
            print('You chose scissors, computer chose scissors')
            return 1


def printScores(scores):
    print('Final Scores:')
    scoresLen = [0, 0, 0]
    maxLen = 0

    for i in range(0, len(scores)):
        scores[i] = str(scores[i])
        scoresLen[i] = len(scores[i])
        maxLen = max(maxLen, scoresLen[i])

    for i in range(0, len(scores)):
        while scoresLen[i] < maxLen:
            scores[i] = ' ' + scores[i]
            scoresLen[i]+=1

    print('Computer Wins: ' + scores[0])
    print('Ties:          ' + scores[1])
    print('Your Wins:     ' + scores[2])


def main():
    scores = [0, 0, 0]
    while True:
        computer = random.randint(0, 2)
        player = input('Rock, paper, or scissors? ')
        if checkInput(player):
            winner = compare(computer, player)
            scores[winner]+=1

            if winner == 0: print('Computer Wins!')
            elif winner == 1: print('Tie!')
            else: print('You Win!')

        else:
            if (player == 'done' or player == 'stop'):
                printScores(scores)
                break
            print('Invalid input!')
            continue



if __name__ == '__main__':
    main()