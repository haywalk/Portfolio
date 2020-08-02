'''
Insertion sort algorithm
Hayden Walker
1 August 2020
'''

def insertionSort(listIn):
	# Starting with the second item in the list, iterate through the list
	for item in range(1, len(listIn)):
		indexToTest = item # Get the index we'll be sorting
		indexToSwap = item - 1 # Get the index we'll be testing the previous one against
		
		# Check all previous indexes for a smaller value than the one we're sorting
		while indexToSwap >= 0:
			if listIn[indexToTest] < listIn[indexToSwap]:
				# If a smaller value is found, swap them
				listIn[indexToTest], listIn[indexToSwap] = listIn[indexToSwap], listIn[indexToTest] 
				# Set the test index to the one we swapped with
				indexToTest = indexToSwap
			# Move back an index
			indexToSwap -= 1

	# Return the sorted list
	return listIn

toSort = [13, 16, 9, 22, 29, 3]

print(insertionSort(toSort))
