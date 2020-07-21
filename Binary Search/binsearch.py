'''
Recursive binary search algorithm
Hayden Walker
21 July 2020
'''

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
		return None

# The array and the target
myArray = [1, 8, 9, 12, 16, 82, 92, 120]
target = 0

print(binarySearch(len(myArray), 0, target))
