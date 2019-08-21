def getvals():
	bal = float(input("Total: "))
	tend = float(input("Tendered: "))
	getchange(bal, tend)

def getchange(bal, tend):
	due = round((tend - bal), 2)

	nickels = 0
	dimes = 0
	quarters = 0
	loonies = 0
	toonies = 0
	fives = 0
	tens = 0
	twenties = 0
	fifties = 0

	if due == 0:
		print(f"Change due: {due}")
		print("Sale complete.")
		input("Press ENTER to continue...")
		getvals()
	elif due < 0:
		print("Insufficient funds!")
		input("Press ENTER to continue...")
		getvals()
	else:
		print(f"Change due: {due}")

		while due > 0:
			if due >= 50:
				fifties += 1
				due -= 50
			elif due >= 20:
				twenties += 1
				due -= 20
			elif due >= 10:
				tens += 1
				due -= 10
			elif due >= 5:
				fives += 1
				due -= 5
			elif due >= 2:
				toonies += 1
				due -= 2
			elif due >= 1:
				loonies += 1
				due -= 1
			elif due >= 0.25:
				quarters += 1
				due -= 0.25
			elif due >= 0.10:
				dimes += 1
				due -= 0.10
			elif due >= 0.05:
				nickels += 1
				due -= 0.05
			elif due >= 0.03:
				nickels += 1
				due = 0
			else:
				due = 0

		if fifties > 0: print(f"	-> $50.00 x {fifties}")
		if twenties > 0: print(f"	-> $20.00 x{twenties}")
		if tens > 0: print(f"	-> $10.00 x{tens}")
		if fives > 0: print(f"	-> $ 5.00 x{fives}")
		if toonies > 0: print(f"	-> $ 2.00 x{toonies}")
		if loonies > 0: print(f"	-> $ 1.00 x{loonies}")
		if quarters > 0: print(f"	-> $ 0.25 x{quarters}")
		if dimes > 0: print(f"	-> $ 0.10 x{dimes}")
		if nickels > 0: print(f"	-> $ 0.05 x{nickels}")

		getvals()

getvals()
