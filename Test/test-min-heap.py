import unittest
from MinHeap import MinHeap


class TestConstructor(unittest.TestCase):
    def initialization_testing_0(self):
        arr = []
        heap = MinHeap(arr)
        self.assertEqual(heap.array(), [])

    def initialization_testing_1(self):
        arr = [1]
        heap = MinHeap(arr)
        self.assertEqual(heap.array(), [1])

    def initialization_testing_2(self):
        arr = [3, 1]
        heap = MinHeap(arr)
        self.assertEqual(heap.array(), [1, 3])

    def initialization_testing_3(self):
        arr = [10, 3, 1, 4, 6, 5, 13, 9, 8, 17, 15]
        heap = MinHeap(arr)
        self.assertEqual(heap.array(), [1, 4, 3, 8, 6, 5, 13, 10, 9, 17, 15])

if __name__ == '__main__':
    unittest.main()

