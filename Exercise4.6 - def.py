# Rewrite your pay computation with time-and-a-half (1.5) for over-
# time and create a function called 'computepay' which takes two parameters
# (hours and rate).

#..............

# def_ indicates the start of a function.
# It indicates that the following indented section of code is to be stored for later

def computepay(hrs, rate): 
	if hrs > 40:
		income = (hrs - 40)*1.5*rate + (40*rate)
	else:
		income = hrs*rate
	return print('Pay:',income)

hrs = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
computepay(hrs,rate)

input('\nPress ENTER to exit')
