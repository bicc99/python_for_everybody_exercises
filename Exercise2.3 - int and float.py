hours = int(input("Enter hour: "))
# No print() here. It includes in input()
rates = float(input("Enter rate: "))

income = hours * rates
print("Pay:", income)

input("\nPress ENTER to exit >>")