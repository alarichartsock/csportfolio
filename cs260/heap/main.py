"""
    Binheap Runner
"""
from random import randint
import binheap as bin


def random_list(low=0, high=100, count=20):
    return [randint(low, high) for _ in range(count)]


def main():
    nums = random_list(count=10)
    print("List:", nums)
    heap = bin.BinHeap(False)
    heap.build_heap(nums)
    print("Heap:", heap)
    heap.sort()
    print("Sorted:", heap)


if __name__ == "__main__":
    main()