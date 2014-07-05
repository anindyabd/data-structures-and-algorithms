class BinHeap:
    """A priority queue implemented as a binary heap.
    In a binary heap, children are at locations i*2 and i*2 + 1.
    Parents are always at i//2 (integer divison)."""

    def __init__(self):
        """A binary heap uses a complete tree.
        Therefore we can just use a list to represent it.
        """
        self.heapList = [0] #The first element is zero.
                            #This zero is not used -- it's there so that integer divison
                            #for access works in later methods.
        self.currentSize = 0

    def percUp(self, i):
        """
        This private method causes the element at 
        index i to percolate up until the heap order property
        is assured -- i.e. all parents are smaller than their children.
        Sadly, private methods in Python aren't *truly* private as they are in 
        Java.
        """
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, item):
        """Inserts an item in the heap."""
        self.heapList.append(item)
        self.currentSize += 1 
        self.percUp(self.currentSize)

    def percDown(self, i):
        """This private method helps delMin. After the last element in the 
        heap is substituted for the root in delMin, this makes that element
        percolate down the heap to its proper place so that the heap order 
        is restored.
        """
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[mc] < self.heapList[i]:
                tmp = self.heapList[mc]
                self.heapList[mc] = self.heapList[i]
                self.heapList[i] = tmp
            i = mc

    def minChild(self, i):
        """This helper method is for percDown. It returns the index 
        of the minimum child of the element at i."""
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if min(self.heapList[i*2], self.heapList[(i*2)+1]) == self.heapList[i*2]:
                return i*2
            else:
                return i*2 + 1

    def delMin(self):
        """Deletes the smallest element -- i.e. the first element in the heap.
        Replaces that with the last element in the heap and then percolates down.
        """
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize -= 1
        self.percDown(1)

    def findMin(self):
        """Returns the minimum element in the heap,
        i.e. the element at the root (because this is a min heap)."""
        return self.heapList[1]

    def buildHeap(self, alist):
        """Builds a heap given a list of values.
        Running time of this is O(n)."""
        i = len(alist) // 2 
        self.currentSize = len(alist)
        self.heapList = [0] + alist
        while i > 0:
            self.percDown(i)
            i = i - 1

def test():
    pq = BinHeap()
    pq.buildHeap([9,6,5,2,3])
    assert(pq.heapList == [0,2,3,5,6,9])






