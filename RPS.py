import random
import re
import time


class RPS:

    def __init__(self, name, rounds):
        self.name = name
        self.totalRounds = rounds
        self.roundsRemaining = rounds
        self.player_score = 0
        self.computer_score = 0
        self.player_choice = ''
        self.play()

    def askPlayer(self):
        self.player_choice = input('Choose between Rock(R), Paper(P) and Scissor(S)')[0].lower()

    def choiceToInt(self):
        return 1 if self.player_choice == 'r' else 2 if self.player_choice == 'p' else 3

    def intToChoice(self, choice):
        return 'rock' if choice == 1 else 'paper' if choice == 2 else 'scissor'

    def differenceToWinner(self, compChoice):
        diff = self.choiceToInt() - compChoice
        if diff == 0:
            return f'It is a draw, the computer also picked {self.intToChoice(compChoice)}.' \
                   f' {self.totalRounds-self.roundsRemaining}/{self.totalRounds}'
        elif diff == -2 or diff == 1:
            self.player_score += 1
            return f'You won, the computer picked {self.intToChoice(compChoice)}.' \
                   f' {self.totalRounds-self.roundsRemaining}/{self.totalRounds}'
        else:
            self.computer_score += 1
            return f'You lost, the computer picked {self.intToChoice(compChoice)}.' \
                   f' {self.totalRounds-self.roundsRemaining}/{self.totalRounds}'

    def play(self):
        while self.roundsRemaining > 0:
            self.askPlayer()
            print('\n' * 10)
            self.roundsRemaining -= 1

            acceptedAns = False
            while not acceptedAns:
                if re.search(f'-{self.player_choice}', '-rock-paper-scissor'):
                    print(self.differenceToWinner(random.randrange(1, 4)))
                    acceptedAns = True
                else:
                    print(f'{self.player_choice} is not a valid response!')
                    self.askPlayer()

        self.endGame()

    def endGame(self):
        print(f'Well played! The final result is\n'
              f'{self.name}: {self.player_score}\n'
              f'Mr.Rock: {self.computer_score}')
        time.sleep(2)
        acceptedAns = False
        while not acceptedAns:
            cont = input('Would you like to play again? Yes(Y)/No(N)')
            if re.search(f'{cont}', 'yes'):
                newGame()
                acceptedAns = True
            elif re.search(f'{cont}', 'no'):
                print(f'Alright, bye it was fun while it lasted, {self.name}! :/')
                exit(1)
            else:
                print(f'{self.player_choice} is not a valid response!')


def newGame():
    name = input('Hello, my name is Mr. Rock and you are?')
    rounds = int(input(f'Oh, hello {name}! How many rounds would you like to play?'))

    RPS(name, rounds)


newGame()
