class maxHeap:

    def __init__(self, heap=None):
        self.__heap = [] if heap is None else self.build_max_heap(heap)
    
    def getHeap(self):
        return self.__heap

    def getSize(self):
        return self.__heapSize

    def toString(self):
        return str(self.__heap)

    def parent(self, i):
        return(i // 2)

    def leftChild(self, i):
        return(i * 2)

    def rightChild(self, i):
        return(2 * i + 1)

    def max_heapify(self, i, h):
        r = self.rightChild(i)
        l = self.leftChild(i)
        largest = 0

        if(l < len(h)  and h[l] > h[i]):
            largest = l
        else:
            largest = i

        if(r < len(h)  and h[r] > h[largest]):
            largest = r

        if(largest != i):
            h[i], h[largest] = h[largest], h[i]
            self.max_heapify(largest, h)

    def build_max_heap(self, h):
        for i in range(len(h)//2, -1, -1):
            self.max_heapify(i, h)
        return h

    def maximum(self):
        return self.__heap[0]

    def insert(self, i):
        h = self.__heap
        h.append(i)
        self.__heap = self.build_max_heap(h)

    @staticmethod
    def heapSort(a):
        a = maxHeap(a).getHeap()
        h = []
        for i in range(0,len(a)):
            h = [a[0]] + h
            a = maxHeap(a[1:]).getHeap()

        return h



class minHeap:

    def __init__(self, heap=None):
        self.__heap = [] if heap is None else self.build_min_heap(heap)

    def getHeap(self):
        return self.__heap

    def getSize(self):
        return self.__heapSize

    def toString(self):
        return str(self.__heap)

    def parent(self, i):
        return(i // 2)

    def leftChild(self, i):
        return(i * 2)

    def rightChild(self, i):
        return(2 * i + 1)

    def min_heapify(self, i, h):
        r = self.rightChild(i)
        l = self.leftChild(i)
        smallest = 0

        if(l < len(h)  and h[l] < h[i]):
            smallest = l
        else:
            smallest = i

        if(r < len(h)  and h[r] < h[smallest]):
            smallest = r

        if(smallest != i):
            h[i], h[smallest] = h[smallest], h[i]
            self.min_heapify(smallest, h)

    def build_min_heap(self, h):
        for i in range(len(h)//2, -1, -1):
            self.min_heapify(i, h)
        return h

    def minumum(self):
        return self.__heap[0]

    def insert(self, i):
        h = self.__heap
        h.append(i)
        self.__heap = self.build_min_heap(h)

    @staticmethod
    def heapSort(a):
        a = minHeap(a).getHeap()
        h = []
        for i in range(0,len(a)):
            h = h+ [a[0]]
            a = minHeap(a[1:]).getHeap()

        return h

class priorityQueue(maxHeap):
    def heap_extract_max(self, a):
        if(len(a) < 1):
            return "heap underflow"
        max = a[0]
        a[0] = a[len(a)-1]
        a = self.build_max_heap(a[1:])
        self.__heap = a
        return max

    def heap_increase_key(self, a, i, k):
        if(k < a[i]):
            return "New key is smaller then current key"
        a[i] = k
        while i > 1 and a[self.parent(i)] < a[i]:
            a[i], a[self.parent(i)] = a[self.parent(i)], a[i]
            i = self.parent(i)
        self.__heap = a

