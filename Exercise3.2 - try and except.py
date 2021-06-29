num_hrs = input('Enter Hours: ')
num_rate = input('Enter Rate: ')

try:
    hrs = float(num_hrs)
    rate = float(num_rate)
except:
    print(input('\nError, Please enter numeric input'))
    quit() #to stop running another lines

bill = hrs*rate
print('Pay: ',bill)

input('Press ENTER to exit >>')
