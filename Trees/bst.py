class BinarySearchTree:
    """A binary tree that follows the property 
    that all *keys* smaller than a parent are to
    its left and all larger are to its right.
    """
    
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        """Private length method."""
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        """Inserts a key-value pair into the tree."""
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1
 
    def _put(self, key, val, currentNode):
        """Private method that does the actual work
        of putting a key-value pair into the tree. Encapsulation,
        baby.
        """
        if currentNode.key > key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val)
                currentNode.leftChild.parent = currentNode        
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val)
                currentNode.rightChild.parent = currentNode

    def get(self, key):
        """Gets the value associated with a key."""
        return self._get(key, self.root)

    def _get(self, key, currentNode):
        """Private method that does the actual work of 
        getting the value."""
        if not currentNode:
            return None
        if currentNode.key == key:
            return currentNode.payload
        if currentNode.key > key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

class TreeNode:

    def __init__(self, key, val,
                left=None, right=None, parent=None):

        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right 
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild  

    def isLeftChild(self):
        return self.parent and self.parent.leftChild 

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value 
        self.leftChild = lc
        self.rightChild = rc 
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self 

def test():
    bst = BinarySearchTree()
    bst.put(5, 'five')
    bst.put(3, 'three')
    bst.put(4, 'four')
    print(bst.root.hasLeftChild())
    print(bst.root.hasRightChild())
    print(bst.root.leftChild.hasRightChild())
    print(bst.get(3))
    print(bst.get(4))
    print(bst.get(5))  

test()     

