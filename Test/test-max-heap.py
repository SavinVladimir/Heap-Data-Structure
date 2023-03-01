import unittest
from MaxHeap import MaxHeap


class TestConstructor(unittest.TestCase):
    def initialization_testing_0(self):
        arr = []
        heap = MaxHeap(arr)
        self.assertEqual(heap.array(), [])

    def initialization_testing_1(self):
        arr = [1]
        heap = MaxHeap(arr)
        self.assertEqual(heap.array(), [1])

    def initialization_testing_2(self):
        arr = [1, 3]
        heap = MaxHeap(arr)
        self.assertEqual(heap.array(), [3, 1])

    def initialization_testing_3(self):
        arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
        heap = MaxHeap(arr)
        self.assertEqual(heap.array(), [17, 15, 10, 8, 13, 3, 6, 1, 5, 4, 9])


if __name__ == '__main__':
    unittest.main()
