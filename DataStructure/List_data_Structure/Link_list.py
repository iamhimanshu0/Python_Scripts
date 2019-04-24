class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	#print the data inside the list
	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next


	# add the data in last pos
	def append(self,data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	# add the data in the first pos
	def add_first(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	# add node into given point
	def add_given_point(self,perv_node,data):
		new_node = Node(data)
		new_node.next = perv_node.next
		perv_node.next = new_node
 
	#delete the node
	def delete_node(self,key):
		cur_node = self.head
		# check for the head node
		if cur_node and cur_node.data == key:
			self.head = cur_node.next
			cur_node = None

		perv_node = self.head
		while cur_node and cur_node.data != key:
			perv_node = cur_node
			cur_node = cur_node.next
			

		perv_node.next = cur_node.next
		cur_node.next = None


	# delete the node form the given pos
	
	def delete_data_at_give_pos(self,value):
		count = 0
		cur_node = self.head
		if value == 0:
			 self.head = cur_node.next
			 cur_node = None
			 return

		perv_node = self.head
		while cur_node and count != value:
			count+=1
			perv_node = cur_node
			cur_node  = cur_node.next

		perv_node.next = cur_node.next
		cur_node.next = None

	
	# Find the lenght of a LinkedList
	def find_len(self):
		cur_node = self.head
		count = 0
		while cur_node:
			count+=1
			cur_node = cur_node.next

		print(count)
		print("-------------")

	
	# find the lenght of a LinkedList using Recursive way
	def len_recursive(self,node):
		if node is None:
			return 0
		return 1+self.len_recursive(node.next)

	# swap the values of two node
	def swap_node(self,key_1,key_2):
		if key_1 == key_2:
			return

		cur_1 = self.head
		perv_1 = None

		while cur_1 and cur_1.data != key_1:
			perv_1 = cur_1
			cur_1 = cur_1.next

		cur_2 = self.head
		perv_2 = None
		while cur_2 and cur_2.data != key_2:
			perv_2 = cur_2
			cur_2 = cur_2.next
	# not complete yet
		

		
				


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.swap_node("B","C")
# llist.find_len()
# print(llist.len_recursive(llist.head))
# llist.delete_data_at_give_pos(0)
# llist.delete_node("B")
# llist.add_first("D")
# llist.add_given_point(llist.head,'D')
llist.print_list()

