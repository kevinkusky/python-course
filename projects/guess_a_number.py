import random

current_guesses = 0

print('Hello, I want to play a game!')
name = input('What is your name?')

game_number = random.randint(1, 20)

print(f'Well {name}, I am thinking of a number between 1 and 20!')

while current_guesses < 6:
    guess = int(input('Take a guess?'))
    current_guesses += 1
    if guess == game_number:
        break
    elif guess < game_number:
        print(f'Your guess of {guess} was too low.')
    elif guess > game_number:
        print(f'Your guess of {guess} was too high.')


if guess == game_number:
    print(f'Congrats {name}, You guessed {game_number} in {current_guesses} guesses!')
else:
    print(f"Sorry, {name}. You could not guess my number {game_number}.")