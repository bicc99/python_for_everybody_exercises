# Write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range, print an error message. If the score is
# between 0.0 and 1.0, print a grade using the following table:
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly as shown above to test the various different values for input.

score_input = input('Enter score: ')
try:
    score = float(score_input)
except:
    print('Bad score')
    input() #to hold and ENTER to close the prompt

if score >= 0 and score <= 1:
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    elif score < 0.6:
        grade = 'F'
else: # It can be coded without else_func
    print('Error, the score is out of range')
    input()  # to hold and ENTER to close the prompt

print('Your garde is',grade)

input('\nPress ENTER to exit >>')
