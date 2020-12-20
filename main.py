

class Edge:
	def __init__(self, edge_str, side):
		self.edge = edge_str
		self.side = side

	def compare_edge(self, other_edge):
		howtorotate = 0
		flipx = None
		flipy = None

		same_edge = False
		flipped_edge = None
		if self.edge == other_edge.edge:
			same_edge = True
			flipped_edge = False
		elif self.edge[::-1] == other_edge.edge:
			same_edge = True
			flipped_edge = True

		if same_edge:
			if self.side == 'top': 
				if other_edge.side == 'top':
					flipy = True
					flipx = False
					howtorotate = 0
				elif other_edge.side == 'right':
					flipy = False
					flipx = True
					howtorotate = 270
				elif other_edge.side == 'bottom':
					flipy = False
					flipx = False
					howtorotate = 0
				elif other_edge.side == 'left':
					flipy = False
					flipx = False
					howtorotate = 270
			if self.side == 'right': 
				if other_edge.side == 'top':
					flipy = True
					flipx = False
					howtorotate = 90
				elif other_edge.side == 'right':
					flipy = True
					flipx = False
					howtorotate = 270
				elif other_edge.side == 'bottom':
					flipy = False
					flipx = False
					howtorotate = 90
				elif other_edge.side == 'left':
					flipy = False
					flipx = False
					howtorotate = 0
			if self.side == 'bottom': 
				if other_edge.side == 'top':
					flipy = False
					flipx = False
					howtorotate = 0
				elif other_edge.side == 'right':
					flipy = False
					flipx = False
					howtorotate = 270
				elif other_edge.side == 'bottom':
					flipy = True
					flipx = False
					howtorotate = 0
				elif other_edge.side == 'left':
					flipy = True
					flipx = False
					howtorotate = 90
			if self.side == 'left': 
				if other_edge.side == 'top':
					flipy = False
					flipx = False
					howtorotate = 90
				elif other_edge.side == 'right':
					flipy = False
					flipx = False
					howtorotate = 0
				elif other_edge.side == 'bottom':
					flipy = False
					flipx = True
					howtorotate = 270
				elif other_edge.side == 'left':
					flipy = False
					flipx = True
					howtorotate = 0

		if flipped_edge:
			flipx = not flipx
			flipy = not flipy

		return same_edge, flipx, flipy, howtorotate, self.side, other_edge.side

class Tile:
	def generate_edges(self):
		edges = []

		edges.append(Edge(self.data[0], 'top'))
		edges.append(Edge(self.data[-1], 'bottom'))

		left_side = ''
		right_side = ''
		for data in self.data:
			left_side += data[0]
			right_side += data[-1]

		edges.append(Edge(left_side, 'left'))
		edges.append(Edge(right_side, 'right'))
 
		return edges
			
	def rotate(self, degrees):
		new_data = [''] * len(self.data)
		if degrees == 90:
			for row in self.flip('y').data:
				for letter_pos, letter in enumerate(row):
					new_data[letter_pos] = new_data[letter_pos] + letter

			return Tile(self.id, new_data)
		if degrees == 180:
			return self.rotate(90).rotate(90)
		if degrees == 270:
			return self.rotate(90).rotate(90).rotate(90)

	def flip(self, how):
		if how == 'y':
			self.data = self.data[::-1]

			return Tile(self.id, self.data)

		if how == 'x':
			new_data = []
			for row in self.data:
				new_data.append(row[::-1])
			self.data = new_data

			return Tile(self.id, self.data)


	def __init__(self, tile_id, tile_data):
		self.id = tile_id
		self.data = tile_data #will be an array with strings ex ['##..#', '...##']
		self.edges = self.generate_edges()

tile1 = Tile('1', ['##..', '.##.', '##.#', '###.'])
tile2 = Tile('2', ['##.#', '###.', '.#.#', '#.##'])

print([edge.side + edge.edge for edge in tile1.edges])
print([edge.side + edge.edge for edge in tile2.edges])

for edge1 in tile1.edges:
	for edge2 in tile2.edges:
		same, flipx, flipy, rotate, this_side_rot, other_side_rot = edge1.compare_edge(edge2)
		if same:
			print(flipx, flipy, rotate, this_side_rot, other_side_rot)
			break

print(tile1.data)
if flipx:
	tile2 = tile2.flip('x')
if flipy:
	tile2 = tile2.flip('y')
if rotate != 0:
	tile2 = tile2.rotate(rotate)

print(tile2.data)

List_of_tiles = []
# Tile Data Parsing
with open('example_input.txt', 'r') as input_data:
	input_data_array = input_data.read().split('\n\n')
	for tile in input_data_array:
		tile_id = tile.split('\n')[0].split(' ')[1][:-1]
		tile_data = tile.split('\n')[1:]
		List_of_tiles.append(Tile(tile_id, tile_data))

for tile in List_of_tiles[1:]:
	for test_tile_edge in tile.edges:
		for main_tile_edge in List_of_tiles[0].edges:
			if main_tile_edge.edge == test_tile_edge.edge:
				print(main_tile_edge, test_tile_edge)

"""
.#.#
.###
.#.#
....
"""


"""
##..
.##.
##.#
###.

.#.#
.###
.#.#
....
"""

"""
123
456
789

789
456
123



741
852
963

"""