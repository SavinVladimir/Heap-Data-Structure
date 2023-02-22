class MinHeap:
    def __init__(self, h=None):
        if h is None:
            h = []
        self.heap = []
        self.size = -1
        for el in h:
            self.insert(el)

    def siftUp(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] <= self.heap[index]:
                break
            self.swap(parent, index)
            index = parent

    def siftDown(self, index):
        while 2 * index + 1 < self.size:
            left = 2 * index + 1
            right = 2 * index + 2
            j = left
            if right < self.size and self.heap[right] < self.heap[left]:
                j = right
            if self.heap[index] <= self.heap[j]:
                break
            self.swap(index, j)
            index = j

    def swap(self, first: int, second: int):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]

    def insert(self, k: int):
        self.heap.append(k)
        self.size += 1
        self.siftUp(self.size)

    def extract(self):
        if self.size > 0:
            self.heap[0] = self.heap[self.size]
            self.siftDown(0)
        del self.heap[self.size]
        self.size -= 1

    def min_value(self):
        return self.heap[0]

    def array(self):
        return self.heap
