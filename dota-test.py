import random
from time import sleep
import webbrowser
import sys

yes = {'yes','y', ''}
no = {'no','n'}
year = 2020

print('How old are you? ', end='')
my_age = input()

if float(my_age) >= 0:
    print('You from Russia? [y/n]: ', end='')
    choice = input().lower()
    if choice in yes:
        your_age_of_dead = 77 - float(my_age) + random.randint(1,5)
        print('Processing your data... ')
        for i in range(21):
            sys.stdout.write('\r')
            sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
            sys.stdout.flush()
            sleep(0.25)
        print(' ')
    elif choice in no:
        sys.stdout.write("Migrate to Russia")
    else:
        sys.stdout.write("Please respond with 'yes' or 'no'")
        exit(1)
    if float(my_age) >= 18:
        print('You must drink vodka and play dotka')
        webbrowser.open('steam://rungameid/570', new=1)
    else:
        print('You will still live approximately: {0}'.format(your_age_of_dead))
else:
    print('Lie is for bitches')