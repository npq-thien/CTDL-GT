import rbt
bst = rbt.RedBlackTree()

bst.insert(54)
bst.insert(40)
bst.insert(65)
bst.insert(60)
bst.insert(75)
bst.insert(57)

bst.print_tree()

print("\nAfter deleting an element")
bst.delete_node(40)
bst.print_tree()
	