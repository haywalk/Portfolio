'''
Recursive binary search algorithm
Hayden Walker
21 July 2020
'''

# The array and the target
myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 11

def binarySearch(top, bottom, target):
	# Try and look for the target
	try:
		mid = (top + bottom) // 2 # Get midpoint of array

		if myArray[mid] == target: # If the midpoint is the target, then return it
			return mid
		elif myArray[mid] > target: # If mid > target, set the midpoint as the top limit
			return binarySearch(mid, bottom, target)
		elif myArray[mid] < target: # If mid < target, set the midpoint as the bottom limit
			return binarySearch(top, mid, target)

	# If the program reaches max recursion depth, the target isn't there
	except:
		return "null"

print(binarySearch(len(myArray), 0, target))
