class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	# add the data
	def append(self,data):
		if self.head is None:
			new_node = Node(data)
			new_node.prev = None
			self.head = new_node
		else:
			new_node = Node(data)
			cur_node = self.head
			while cur_node.next:
				cur_node= cur_node.next

			cur_node.next = new_node
			new_node.prev = cur_node
			new_node.next = None

	#add data into first
	def add_first(self,data):
		if self.head is None:
			new_node = Node(data)
			# self.head.prev = new_node
			new_node.prev = None
			self.head = new_node
		else:
			new_node = Node(data)
			self.head.prev = new_node
			new_node.next = self.head
			self.head = new_node
			new_node.prev = None

	# add the data after the given Node
	def add_after_node(self,key,data):
		cur_node = self.head
		while cur_node:
			if cur_node.next is None and cur_node.data == key:
				self.append(data)
				return
			elif cur_node.data == key:
				new_node = Node(data)
				nxt = cur_node.next
				cur_node.next = new_node
				new_node.next = nxt
				new_node.prev = cur_node
				nxt.prev = new_node

			cur_node = cur_node.next
			


	# add the data before the given Node
	def add_before_node(self,key,data):
		cur_node = self.head
		while cur_node:
			if cur_node.prev is None and cur_node.data == key:
				self.add_first(data)
				return
			elif cur_node.data == key:
				new_node = Node(data)
				prev = cur_node.prev
				prev.next = new_node
				cur_node.prev = new_node
				new_node.next = cur_node
				new_node.prev = prev
				

			cur_node = cur_node.next


	# delete the Node
	def delete(self,value):
		cur_node = self.head
	
		while cur_node:
			
			if cur_node == self.head and cur_node.data == value:
				# cur_node.prev = None
				# case 1
				if not cur_node.next:
					self.head = None
					cur_node = None
					print("case 1")
					return

				# case 2
				else:
					nxt = cur_node.next
					cur_node.next = None
					# cur_node.prev = None
					nxt.prev = None
					cur_node = None
					self.head = nxt
										
					print("case 2")
					return
			#case 3
			elif cur_node.data == value:
				if cur_node.next:
					nxt = cur_node.next
					prev = cur_node.prev
					prev.next = nxt
					nxt.prev = prev
					cur_node.next = None
					cur_node.prev = None
					cur_node = None
					print('case 3')
					return

				# case 4
				else:
					prev = cur_node.prev
					prev.next = None
					cur_node.prev = None
					cur_node = None
					print('case 4')
					return

		cur_node = cur_node.next


	# print the list
	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next


dlist = DoublyLinkedList()

dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)
dlist.delete(3)
# dlist.add_first(3)
# dlist.add_after_node(1,5)
dlist.print_list()
