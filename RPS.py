import random
import re
import time


class RPS:

    def __init__(self, name, rounds):
        self.name = name # Player name
        self.totalRounds = rounds # Amount of rounds to play
        self.roundsRemaining = rounds # Well rounds remaining?
        self.player_score = 0 # The players score during this match
        self.computer_score = 0 # The computers score during this match
        self.player_choice = '' # The player's score
        self.play() # Start the game

    def askPlayer(self): # Ask the player what they pick for this round
        while True:
            try:
                self.player_choice = input('Choose between Rock(R), Paper(P) and Scissor(S)\n')[0].lower() # Get the first character in the answer lowercased
                break
            except:
                print('There was a problem with your answer. Try again!')
        

    def choiceToInt(self): # Get the numerical representation of the player choice
        return 1 if self.player_choice == 'r' else 2 if self.player_choice == 'p' else 3

    def intToChoice(self, choice): # Almost reverse the choiceToInt function
        return 'rock' if choice == 1 else 'paper' if choice == 2 else 'scissor'

    def handleWinner(self, compChoice): # Decide the winner using a subtraction trick
        diff = self.choiceToInt() - compChoice
        if diff == 0:
            return f'It is a draw, the computer also picked {self.intToChoice(compChoice)}.' \
                   f' {self.totalRounds-self.roundsRemaining}/{self.totalRounds}'  # Return the message for when the user draws
        elif diff == -2 or diff == 1:
            self.player_score += 1
            return f'You won, the computer picked {self.intToChoice(compChoice)}.' \
                   f' {self.totalRounds-self.roundsRemaining}/{self.totalRounds}'  # Return the message for when the user wins
        else:
            self.computer_score += 1
            return f'You lost, the computer picked {self.intToChoice(compChoice)}.' \
                   f' {self.totalRounds-self.roundsRemaining}/{self.totalRounds}'  # Return the message for when the user loses

    def play(self): # The main loop
        while self.roundsRemaining > 0:
            self.askPlayer()
            print('\n' * 2) # Add some space between everything
            self.roundsRemaining -= 1
            while True:
                if re.search(f'-{self.player_choice}', '-rock-paper-scissor'):  # Check if the answer is a valid answer
                    print(self.handleWinner(random.randrange(1, 4)))  # Handle the winner stuff
                    break
                else:
                    print(f'That is not a valid response! Please read the question again!')
                    self.askPlayer()

        self.endGame()

    def endGame(self):
        print(f'\nWell played! The final result is\n' 
              f'You: {self.player_score}\n'
              f'Mr.Rock: {self.computer_score}')  # Say farewell
        time.sleep(2)
        while True:
            cont = input('Would you like to play again? Yes(Y)/No(N)\n')  # Offer a rematch
            if re.match(f'{cont}', 'yes'):
                newGame()  # Start a new game if the user wishes to do so
                break
            elif re.match(f'{cont}', 'no'):
                print(f'Alright, bye it was fun while it lasted, {self.name}! :/')
                exit(1)  # Exit the program if the user does not wish for a rematch
            else:
                print(f'{cont} is not a valid response!')


def newGame():
    name = input('Hello, my name is Mr. Rock and you are?\n')  # Be polite and ask for their name
    while True:
        try:
            rounds = int(input(f'Oh, hello {name}! How many rounds would you like to play?\n'))  # Should be obvious
            if(rounds > 0):
                break
        except ValueError:
            print('You must answer with an positive integer!')

    RPS(name, rounds)  # Initialize a new game or somethign


newGame()
