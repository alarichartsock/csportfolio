#8: Implement quadratic probing as a rehash technique.

import unittest

class HashTable:
    """Returns a hashTable according to the HashTable ADT on runestone.academy"""

    def __init__(self):
        """Initializes a hashTable"""
        self.size = 11
        self.usedsize = 0
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        """Puts an item into the hashTable"""
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.usedsize = self.usedsize + 1
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                num = 0;
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    num = num + 1
                    nextslot = self.rehash(nextslot, len(self.slots),num)

                if self.slots[nextslot] == None:
                    self.usedsize = self.usedsize + 1
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.size = self.size + 1
                    self.data[nextslot + 1] = data

    def hashfunction(self, key, size):
        """Hashes an input"""
        return key % size

    def rehash(self, oldhash, size,num):
        """Rehashes the hashtable"""
        return ((oldhash+1) % size) + num**2

    def get(self, key):
        """Gets an item from a hashtable"""
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and  \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        """Gets an item from the hashtable"""
        return self.get(key)

    def __setitem__(self, key, data):
        """Sets an item in the hashtable"""
        self.put(key, data)

    def __len__(self):
        """Returns length of the hashtable"""
        return self.usedsize

    def __contains__(self,item):
        """Returns whether or not something is inside of the hashTable"""
        if item in self.data:
            return True
        else:
            return False

    def __del__(self):
        """Deletes hashtable"""

class testList(unittest.TestCase):
    """Tests the hashTable, acts as a main driver"""
    def testHashTable(self):
        """Tests hashtable length"""
        h = HashTable()
        h.put(1,1)
        h.put(2,2)
        h.put(3,3)
        h.put(4,4)
        self.assertEqual(len(h),4)
        self.assertEqual(1 in h,True)
        del h
        
if __name__ == '__main__':
    unittest.main()