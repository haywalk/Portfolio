'''
Roman numeral to integer converter
Hayden Walker, 19 January 2020
'''
romanNum = input().upper()
parts = list()
num = 0

romanLets = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }

for let in romanNum:
	'''
	Replace the letters with the values they represent
	'''
	parts.append(romanLets[let])

for part in parts:
	ind = parts.index(part)
	
	# If not at the end & number is greater than next index, subtract it
	if ind != len(parts) - 1:
		if part < parts[ind + 1]:
			num -= part
			continue

	# Otherwise add the number
	num += part

print(num)
