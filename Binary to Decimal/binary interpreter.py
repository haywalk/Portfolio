'''
Binary interpreter
Hayden Walker, 18 September
'''

nums = input().split() # Split the string into individual values
output = str() # Create the output string

for byte in nums:
	byte = byte[::-1] # Reverse the byte so that its indexes correspond to powers
	out, pos = 0, 0 # Counters for the byte's value, as well as what byte is being counted

	for bit in byte:
		if int(bit): # 1 = True
			out += 2 ** pos
		pos += 1

	output += str(out) + " " # Concatenate the value onto the output string

print(output)
