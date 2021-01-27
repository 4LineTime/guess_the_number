import random
import sys

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 500


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    try:
        print("WELCOME To guess the number program ")
        
        guess=int(input('Guess the secret number? '))
    except ValueError:
        print('you have entered non-integer input. please try again')
        sys.exit(1) #exit the code after error
        
    return guess


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            again = input('Would you like to play again? (y/n)')[0].lower()
            if again !='y':
                print('Thanks for playing!')
                break
            




if __name__ == '__main__':
    main()
