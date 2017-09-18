
# Node in a grid
class Node:
	def __init__(self, pos, cost):
		self.pos = pos
		self.cost = cost

# Grid representation of the graph
class Grid:

	# constructor
	def __init__(self, vals, width, height):

		self.grid = [[None] * width for _ in range(height)]

		self.width = width
		self.height = height

		for y in range(self.height):
			for x in range(self.width):
				self.grid[y][x] = Node((x, y), vals[y][x])

	# get a list of valid neighboring nodes for the given position (x,y)
	def get_neighbors(self, pos):
		x, y = pos
		ns = []

		if y + 1 < self.height:
			ns.append(self.grid[y + 1][x])
		if y - 1 >= 0:
			ns.append(self.grid[y - 1][x])
		if x + 1 < self.width:
			ns.append(self.grid[y][x + 1])
		if x - 1 >= 0:
			ns.append(self.grid[y][x - 1])

		return (n for n in ns if n is not None)

	# get the node at a specified position (x,y)
	def get_node(self, pos):
		return self.grid[pos[1]][pos[0]]

# dijkstra's algorithm for finding the shortest path
# since we only care about the distance (cost) we don't need to store the path
def dijkstra(grid, start, goal):

	unvisited = set()
	dist = dict()

	# initialize the distance array for each node to the max distance and add to unvisited
	for y in range(grid.height):
		for x in range(grid.width):
			dist[(x, y)] = grid.height * grid.width * 2
			unvisited.add((x, y))

	dist[start] = grid.get_node(start).cost

	# end when there are no unvisited node (meaning no path) which shouldn't happen in this scenario
	while len(unvisited) > 0:

		# get the node with the least distance from start
		curr = list(unvisited)[0]
		for n in unvisited:
			if dist[n] < dist[curr]:
				curr = n

		unvisited.remove(curr)

		# end if the current node is the end node (found shortest path), return distance
		if curr == goal:
			return dist[curr]

		# change the distance/cost to go to the neighbors with the lesser one
		neighbors = grid.get_neighbors(curr)
		for n in neighbors:
			new_cost = dist[curr] + n.cost
			if new_cost < dist[n.pos]:
				dist[n.pos] = new_cost

	# shouldn't happen
	return -1

# Input
with open("sum.in") as f:
	r, c = (int(x) for x in f.readline().split(' '))
	nums = [[int(x) for x in l.split(" ") if x.strip() != ""] for l in f.readlines()]

# initialize grid
grid = Grid(nums, c, r)
# calculate sum of shortest distance
total = dijkstra(grid, (0, 0), (c - 1, r - 1))

# Output
with open("sum.out", "w") as f:
	f.write(str(total))

