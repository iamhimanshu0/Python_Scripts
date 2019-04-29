class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    # print tree
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(tree.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(tree.root, '')
        else:
            print(f'Traversal type {str(traversal_type)} is not supported')
            return False

    # preorder tree
    def preorder_print(self, start, traversal):
        '''Root->Left->Right'''
        if start:
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


    # inorder tree
    def inorder_print(self, start, traversal):
        '''Left->Rott->Right'''
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    # postorder tree
    def postorder_print(self, start, traversal):
        '''Left->Right->Root'''
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal


# set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
# tree.root.right.right.right = Node(8)

print(tree.print_tree('preorder'))
print('-----------------')
print(tree.print_tree('inorder'))
print('------------------')
print(tree.print_tree('postorder'))
