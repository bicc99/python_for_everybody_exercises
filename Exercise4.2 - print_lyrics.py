#  Move the last line of this program to the top, so the function
#  call appears before the definitions. Run the program and see what error
#  message you get.
# Answer: NameError: name 'repeat_lyrics' is not defined

repeat_lyrics()

input()

def reprint_lyrics():
	print_lyrics()

def print_lyrics():
	print('All the days, all the nights')
	print('I will be by your side')
	print('No, we dont have to rush')
	print('We can take our time\n\n')

def repeat_lyrics(): # to prepeat
	print_lyrics()   # 1st print_lyrics (the hold block above)
	print_lyrics()	 # 2nd print_lyrics
	print_lyrics()	 # 3rd print_lyrics
repeat_lyrics()      # finis

input('\nPress ENTER to exit >>')