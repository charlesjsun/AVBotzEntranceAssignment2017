
# Input
with open("coins2.in") as f:
	value, *coins = [int(x) for x in f.readline().split()]

# Sort coin values in descending order
coins.sort(reverse=True)

# Dynamic programming

# Store the min number of coins required for each value up to the required value
num_req = [float("inf")] * (value + 1)
num_req[0] = 0

# Loop through each value and find the minimum of coins required for that value and store in the array
for v in range(1, value + 1):
	# try each coin value (similar to the greedy approach)
	for i in range(len(coins)):
		if coins[i] <= v:
			v_left = v - coins[i]
			nq = num_req[v_left]
			# update the num required for this value if it is smaller
			if nq != float("inf") and nq + 1 < num_req[v]:
				num_req[v] = nq + 1

# Output
with open("coins2.out", "w") as f:
	f.write(str(num_req[value]))

