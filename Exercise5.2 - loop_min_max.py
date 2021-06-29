# Write another program that prompts for a list of numbers
# as above and at the end prints out both __"the maximum and minimum"__of
# the numbers instead of the average.

count = 0
# OR min_num = None
# OR max_num = None

while True:
	num_input = input('Enter a number:')
	if num_input == 'done':
	    break
	try:
		numbers = int(num_input)
	except:
		print('Invalid input\n')
		continue

    # consider max & min at first start
	if count == 0:   # OR min_num is None and max_num is None: 
		min_num = numbers
		max_num = numbers
	elif numbers < min_num:
		min_num = numbers
	elif numbers > max_num:
		max_num = numbers

	count = count + 1

print('\nCount:',count,'\nMin:',min_num,'\nMax:',max_num)
input('\nPress ENTER to exit')
