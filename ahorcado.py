import random

class Hangman:
    def __init__(self):
        self.word_list = ['hangman', 'python', 'developer', 'programming', 'challenge']
        self.word = random.choice(self.word_list)
        self guessed_letters = []
        self.chances = 6

    def display(self):
        display_word = ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        print('Current word:', ' '.join(display_word))
        print(f'Chances left: {self.chances}')

    def guess(self, letter):
        if letter in self.guessed_letters:
            print('You already guessed that letter.')
        elif letter in self.word:
            print('Good guess!')
            self.guessed_letters.append(letter)
        else:
            print('Wrong guess!')
            self.guessed_letters.append(letter)
            self.chances -= 1

    def is_finished(self):
        return set(self.word).issubset(set(self.guessed_letters)) or self.chances <= 0

    def play(self):
        print('Welcome to Hangman!')
        while not self.is_finished():
            self.display()
            guess = input('Enter your guess: ').lower()
            if len(guess) == 1 and guess.isalpha():
                self.guess(guess)
            else:
                print('Please enter a valid letter.\n')
        if self.chances > 0:
            print(f'Congratulations! You guessed the word: {self.word}')
        else:
            print(f'Sorry, you ran out of chances. The word was: {self.word}')

if __name__ == '__main__':
    game = Hangman()
    game.play()