
# Input
with open("coins.in") as f:
	value = int(float(f.readline()) * 100)

# Define coin values in cents
coins = [1, 5, 10, 25]

# Greedy method
num = 0  # number of coins
cc = 3  # current coin

while value > 0:
	while coins[cc] > value:
		cc -= 1
	value -= coins[cc]
	num += 1

# Output
with open("coins.out", "w") as f:
	f.write(str(num))

