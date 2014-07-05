class Stack:
	"""
	This uses Python's list data structure for a stack.
	"""

	def __init__(self):
		"""Initializes the stack as an empty list."""
		self.items = []

	def push(self, item):
		"""Pushes an item into the stack
		i.e. appends an item to the end of the list.
		O(1) (amortized)."""
		self.items.append(item)

	def pop(self):
		"""Pops an item off the top of the stack,
		i.e. pops it from the end of the list, 
		and returns it."""
		return self.items.pop()

	def peek(self):
		"""Returns the item on top of the stack."""
		if len(self.items)>0:
			return self.items(len(self.items)-1)
		else:
			return None

	def size(self):
		"""Returns the size of the stack,
		i.e. number of items in the stack."""
		return len(self.items)

	def isEmpty(self):
		"""Returns True if the stack is empty,
		false otherwise."""
		return len(self.items) == 0


