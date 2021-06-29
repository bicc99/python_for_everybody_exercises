# Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out __"the total, count,and average of the numbers"__.
# If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

count = 0
total = 0

while True:
	num_input = input('Enter a number:')
	if num_input == 'done':
	    break
	try:
		numbers = int(num_input)
	except:
		print('Invalid input\n')
		continue
	total = total + numbers
	count = count + 1
	average = float(total / count)

print('Total:',total,'\nCount:',count,'\nAverage:',average)
input('\nPress ENTER to exit')
