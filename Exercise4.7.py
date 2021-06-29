# Rewrite the grade program from the previous chapter using
# a function called 'computegrade' that takes a score as its parameter and
# returns a grade as a string.

def computegrade(score):
    if score >= 0 and score <= 1:
        if score >= 0.9:
            print('Grade: A')
        elif score >= 0.8:
            print('Grade: B')
        elif score >= 0.7:
            print('Grade: C')
        elif score >= 0.6:
            print('Grade: D')
        elif score < 0.6:
            print('Grade: F')
    else:
        print('Error, the score is out of range')
     
try:
	score = float(input('Enter score:'))
except:
	print(input('Bad score\n\nPress ENTER to Exit'))

computegrade(score)
input('\nPress ENTER to exit >>')
