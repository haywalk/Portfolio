'''
24 August 2019
The game guesses a number recursively
'''

def getnum(hi, lo, tries = 0):
	mid = (hi + lo) // 2 # Find the midpoint between the high and low numbers
	tries += 1 # Count up a try

	if input(f"Is the number {mid}? Y/N: ").lower() == "y":
		print(f"I have won! Guessed in {tries} tries.")
		return 0
	else: 
		hilo = input(f"Is the number less than or greater than {mid}? L/G: ")
		if hilo.lower() == "l":
			getnum(mid, lo, tries) # Set the current number as the high point
		elif hilo.lower() == "g":
			getnum(hi, mid, tries) # Set the current number as the low point
		else:
			print("ERR") 

print("Choose a number between 0 and 100 for me to guess.")
getnum(100, 0)
