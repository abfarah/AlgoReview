# AVL Tree:
##### AVL tree's are self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees cannot be more than one for all nodes.
## Operations: h = Height of tree
#### isEmpty: Returns true if BST is empty. – O(1)
#### getBalance(X): Returns the difference between the height in right and left subtrees of x. – O(n)
#### insert(x): Inserts Node(x) into the BST. – O(h)
#### leftRotate(x): Rotates tree x to left whilst maintaining the BST invariant. – O(h)
#### rightRotate(x): Rotates tree x to right whilst maintaining the BST invariant. – O(h)
#### find(x): returns Node containing value x from BST. – O(h)
#### printTree: Prints all the values in the tree using an inorder traversal. – O(n)
#### findMin: Returns the minimum value in the BST. – O(h)
#### findMax: Returns the maximum value in the BST. – O(h)
#### getHeight: Returns the height of the BST. – O(n)
#### isBinarySearchTree(x): Returns True if x is binary search tree and False otherwise: - O(n)
#### Delete(X): Removes a node of value x, and restructures BST to maintain invariant. – O(n) in worst case, O(h) in average case.
#### getSuccessor(x): Gets next successor to given node in BST. – O(h)
## Tree Traversals:
### Depth first: Time complexity: O(n), Space Complexity: O(h)
#### preorder: Traverses the tree recursively in order – root, Left-Subtree, right-Subtree.
#### Postorder: Traverses the tree recursively in order - Left-Subtree, right-Subtree, root.
#### inorder: Traverses the tree recursively in order - Left-Subtree, root, right-Subtree. Returns a sorted list when run on a BST.
### Breadth first: Time complexity: O(n), Space Complexity: O(n)
#### Levelorder: Traverses a list level by level starting at root node. Uses a queue to house nodes. Starts by inserting root into queue. Then dequeuing node, returning its value and then enqueueing its children into queue. This allows us to display each node at each level of the BST.
