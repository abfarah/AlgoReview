# Heaps & Priority Queue
### Heaps: A tree data structure were all nodes can at most have two child nodes.
### Max-Heap: All parent nodes are larger than child nodes.
### Min-Heap: All parent nodes are smaller than child nodes
## Heap as a tree:
#### Root of tree: first element in the array, corresponding to i = 1
#### Parent(i) = floor(i/2): returns index of node’s parent
#### Left(i) = 2i: returns index of node’s left child
#### Right(i) = 2i + 1: returns index of node’s right child
## Heap Operations:
### build_max_heap: O(lg(n))
### max_heapify: O(n lg(n))
### insert: O(): O(lg(n))
### heapsort: O(n lg(n))
# Priority Queue
### Priority Queue: A data structure implementing a set S of elements, each associated with a key, supporting the following operations:
### Maximum(S): O(1)
### extract_max(S): O(lg(n))
### increase_key(S, x, k): O(lg(n))
