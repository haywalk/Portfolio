'''
Caesar cypher by Hayden Walker, 25 July 2019 @ 8:19 PM
'''

# Define the alphabet
alpha = ["", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",\
	"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(msg, key):
	'''
	Create a Caesar cypher using a string and a key
	'''
	# Create a list of cyphered characters
	outstr = list()
	for letter in msg.lower():
		# Check if the character is a letter
		if letter in alpha:
			moved = 0 # Number of spaces moved
			pos = alpha.index(letter) # Letter's initial position
			# Move the character one space at a time
			while moved < key:
				# Check if the letter is at the end of the alphabet
				if pos == 26:
					outstr.append(alpha[key - moved])
					break
				else:
					pos += 1
					moved += 1
			else:
				outstr.append(alpha[pos])
		# If the character is a symbol, simply add it on
		else:
			outstr.append(letter)
	# Return the list joined together into a string
	return "".join(outstr)

# Get a message and an encryption key
msg = input("Message: ")
key = int(input("Key (0-25): "))

# Output the encrypted message
print(caesar(msg, key))

