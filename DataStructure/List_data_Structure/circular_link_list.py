class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class CircularLinkedList:
	def __init__(self):
		self.head = None

	def append(self,data):
		new_data = Node(data)
		

		if self.head is None:
			self.head = new_data
			return
			
		last_node = self.head
		while last_node.next:
			last_node = last_node.next

		last_node.next = new_data

	def print_data(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next


clist = CircularLinkedList()
clist.append('a')
clist.append('b')
clist.append('c')

clist.print_data()
