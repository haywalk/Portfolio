'''
19 July 2019
'''
def piglatin(word):
	'''
	Will convert a string to "Pig-Latin:"
		*If the string begins with a vowel, add "ay" to the end;
		*If the string begins with a consonant, move the first letter to the end and then add "ay."
	It will also capitalize the first letter and make the rest lowercase
	'''
	if word[0] in "aeiou": # Check if the first letter is a vowel - convert to lowercase for simplicity
		latinword = word + "ay" # If so, add "Ay" to the end
	else:
		latinword = word[1:] + word[0] + "ay" # Write from the second letter to the end, then add the first letter, then add "ay"
	return latinword.capitalize() # Return the Pig-Latinized word, with the first letter capitalized and the rest in lowercase

while 1:
	print(piglatin(input("Insert a word: ").lower()))
