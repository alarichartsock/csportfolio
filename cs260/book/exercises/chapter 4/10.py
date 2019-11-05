#10: Implement a radix sorting machine. A radix sort for base 10 integers is a mechanical sorting technique that utilizes a collection of bins, one main bin and 10 digit bins. Each bin acts like a queue and maintains its values in the order that they arrive. The algorithm begins by placing each number in the main bin. Then it considers each value digit by digit. The first value is removed and placed in a digit bin corresponding to the digit being considered. For example, if the ones digit is being considered, 534 is placed in digit bin 4 and 667 is placed in digit bin 7. Once all the values are placed in the corresponding digit bins, the values are collected from bin 0 to bin 9 and placed back in the main bin. The process continues with the tens digit, the hundreds, and so on. After the last digit is processed, the main bin contains the values in order.

class Queue:
    """Abstract Queue implementation, order is LIFO."""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def show(self):
        return self.items

def RadixSort(items):
    mainBin = Queue()
    bin0 = Queue()
    bin1 = Queue()
    bin2 = Queue()
    bin3 = Queue()
    bin4 = Queue()
    bin5 = Queue()
    bin6 = Queue()
    bin7 = Queue()
    bin8 = Queue()
    bin9 = Queue()
    
    #Initial main bin enqueue
    for i in range(len(items)):
        strnum = items[i]
        mainBin.enqueue(items[i])
    
    #Find the longest item
    largest = 0
    for i in range(len(items)):
        if(items[i] > largest):
            largest = items[i]

    #Put items in Buckets

    for i in range(len(str(largest))): #Does as many repetitions as the # of digits on the longest #
        for j in range(len(items)): # loops through the list
            value = mainBin.dequeue()
            index = value % 10**(i+1)
            index = index // 10**i
            if(index == 0):
                bin0.enqueue(value)
            if(index == 1):
                bin1.enqueue(value)
            if(index == 2):
                bin2.enqueue(value)
            if(index == 3):
                bin3.enqueue(value)
            if(index == 4):
                bin4.enqueue(value)
            if(index == 5):
                bin5.enqueue(value)
            if(index == 6):
                bin6.enqueue(value)
            if(index == 7):
                bin7.enqueue(value)
            if(index == 8):
                bin8.enqueue(value)
            if(index == 9):
                bin9.enqueue(value)
        # print("separation")
        # print(bin0.show())
        # print(bin1.show())
        # print(bin2.show())
        # print(bin3.show())
        # print(bin4.show())
        # print(bin5.show())
        # print(bin6.show())
        # print(bin7.show())
        # print(bin8.show())
        # print(bin9.show())
        for i in range(bin0.size()):
            mainBin.enqueue(bin0.dequeue())
        for i in range(bin1.size()):
            mainBin.enqueue(bin1.dequeue())
        for i in range(bin2.size()):
            mainBin.enqueue(bin2.dequeue())
        for i in range(bin3.size()):
            mainBin.enqueue(bin3.dequeue())
        for i in range(bin4.size()):
            mainBin.enqueue(bin4.dequeue())
        for i in range(bin5.size()):
            mainBin.enqueue(bin5.dequeue())
        for i in range(bin6.size()):
            mainBin.enqueue(bin6.dequeue())
        for i in range(bin7.size()):
            mainBin.enqueue(bin7.dequeue())
        for i in range(bin7.size()):
            mainBin.enqueue(bin8.dequeue())
        for i in range(bin7.size()):
            mainBin.enqueue(bin9.dequeue())
    
    final = []
    for i in range(mainBin.size()):
        final.append(mainBin.dequeue())
    return final

print(RadixSort([112,543,313,721,411,456]))

import unittest

class testRadix(unittest.TestCase):
    def testQueue(self):
        self.assertTrue(RadixSort([112,543,313,721,411,456]),[112, 313, 411, 456, 543, 721])
        
if __name__ == '__main__':
    unittest.main()






