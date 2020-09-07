import sys

yes = {'yes','y', ''}
no = {'no','n'}
year = 2020

print('How old are you? ', end='')
my_age = input()

print('How old are your father? ', end='')
father_age = input()

age_of_your_born = float(father_age) - float(my_age)
print('You born when your father was: {0}'.format(age_of_your_born))

print('You from Russia? [y/n]: ', end='')
choice = input().lower()
if choice in yes:
    print('How old are your father? ', end='')
    father_age = input()
elif choice in no:
    sys.stdout.write("Migrate to Russia")
else:
    sys.stdout.write("Please respond with 'yes' or 'no'")

