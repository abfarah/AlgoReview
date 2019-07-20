# Binary Search Tree:
> A binary search tree is a tree data structure that is organized in a binary Tree. A binary tree contains linked nodes that all have three properties, a parent, and two child nodes; a left and right child. The keys in a binary trees are always stored in such a way as to satisfy the binary-search-tree property listed below
Let x be a node in a binary tree. If y is a node in the left subtree of x, then y.key <= x.key. If y is a node in the right subtree of x then y.key >= x.key.
![BST](BST.png)
## Operations:
#### isEmpty: Returns true if BST is empty. – O(1)
#### insert(x): Inserts Node(x) into the BST. – O(h)
#### find(x): returns Node containing value x from BST. – O(h)
#### printTree: Prints all the values in the tree using an inorder traversal. – O(n)
#### findMin: Returns the minimum value in the BST. – O(h)
#### findMax: Returns the maximum value in the BST. – O(h)
#### height: Returns the height of the BST. – O(n)
#### isBinarySearchTree(x): Returns True if x is binary search tree and False otherwise: - O(n)
#### Delete(X): Removes a node of value x, and restructures BST to maintain invariant. – O(n) in worst case, O(h) in average case.
#### getSuccessor(x): Gets next successor to given node in BST. – O(h)
## Binary Tree Traversals:
### Depth first: Time complexity: O(n), Space Complexity: O(h)
#### preorder: Traverses the tree recursively in order – root, Left-Subtree, right-Subtree.
#### Postorder: Traverses the tree recursively in order - Left-Subtree, right-Subtree, root.
#### inorder: Traverses the tree recursively in order - Left-Subtree, root, right-Subtree. Returns a sorted list when run on a BST.
### Breadth first: Time complexity: O(n), Space Complexity: O(n)
#### Levelorder: Traverses a list level by level starting at root node. Uses a queue to house nodes. Starts by inserting root into queue. Then dequeuing node, returning its value and then enqueueing its children into queue. This allows us to display each node at each level of the BST.
