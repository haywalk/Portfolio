'''
 Collatz Conjecture algorithm
'''

import matplotlib.pyplot as plt 

# Get n and define variables
n = int(input("Input n: "))
title = n
step = 0
x = list()
y = list()

x.append(0)
y.append(n)

# Execute the algorithm and add pairs to list
while n > 1:
	if n % 2 == 0:
		n = n // 2
	else:
		n = n * 3 + 1
	step += 1

	print((step, n))
	x.append(step)
	y.append(n)

# Print the number of steps
print(f"Finished in {step} steps.")

# Create the graph
plt.plot(x, y)
plt.title(f"Collatz Conjecture where n is {title} ({step} steps)")
plt.xlabel("Step") 
plt.ylabel('n') 
plt.show() 
