# Trie
#### In computer science, a trie, also called digital tree, radix tree or prefix tree, is a kind of search tree—an ordered tree data structure used to store a dynamic set or associative array where the keys are usually strings. Unlike a binary search tree, no node in the tree stores the key associated with that node; instead, its position in the tree defines the key with which it is associated. All the descendants of a node have a common prefix of the string associated with that node, and the root is associated with the empty string. Keys tend to be associated with leaves, though some inner nodes may correspond to keys of interest. Hence, keys are not necessarily associated with every node. For the space-optimized presentation of prefix tree, see compact prefix tree.
![trie dataStructure](trie.png)
## Operations
#### letterPosition: This method returns the number cooresponding to a letter in the alphabet. I.e the position of 'z' would be 26 since it's last letter in the alphabet.
#### insert: – O(n) were n is the length of the word. This inserts a word into the data structure by creating a node for each individual character in the word.
#### Search:  – O(n) were n is the length of the word. This method returns true if a word exists in the trie data structure and false if the word doesn't exist in the data structure.
