import random

def number_guesser():
    # Create a Number Guesser Game
    num = input('Enter a Number Between 0 and 50: ')
    # Gereate Random Number
    rndNum = random.randint(0, 50)
    # Check If Guess Correct
    if num == rndNum:
        print('Congrats! You guessed correct! The number was ', rndNum)
    else:
        print('You did not guess correct :( \nThe number was ', rndNum, ' and your guess was ', num)

def even_odd():
    # Request a Number
    num = input('Enter a Number: ')
    if int(num)%2 == 0:
        print('Even! ')
    else:
        print('Odd! ')

def length_text():
    # Enter a Piece of Text
    text = input('Enter a piece of text: ')
    print('The sentance is ', len(text), ' charecters long')

#Create a Menu
print('Welcome to the Arcade!')
quit = False
while quit == False:
    print('\nSelect an option from the menu')
    choice = input('1. Number Guesser\n2. Even or Odd\n3. Length of Text\n4. Quit\n')
    if int(choice) == 1:
        number_guesser()
    elif int(choice) == 2:
        even_odd()
    elif int(choice) == 3:
        length_text()
    elif int(choice) == 4:
        quit = True

