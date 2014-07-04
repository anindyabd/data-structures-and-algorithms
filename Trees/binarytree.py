class BinaryTree:
    """A binary tree that uses nodes and references."""

    def __init__(self, rootObj):
        """Initializing the tree."""
        self.key = rootObj 
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        """Creates a new instance of 
        BinaryTree and adds it as a left child."""
        #Two cases are considered. If there's no current left 
        #child, then the new tree is added as the left child.
        #If there's already a left child, the left child that's already 
        #there is pushed down.
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t 

    def insertRight(self, newNode):
        """Creates a new instance of 
        BinaryTree and adds it as a right child."""
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

def buildtree():
    """Builds a tree that you can play around with."""
    tree = BinaryTree('a')
    tree.insertLeft('b')
    tree.insertRight('c')
    tree.leftChild.insertLeft('d')
    tree.leftChild.insertRight('e')
    return tree 

def preorder(tree):
    """External preorder traversal function; code is more elegant!""" 
    if not tree:
        return None
    print(tree.getRootVal())
    preorder(tree.leftChild)
    preorder(tree.rightChild)

def inorder(tree):
    """Inorder traversal"""
    if not tree:
        return None
    inorder(tree.leftChild)
    print(tree.getRootVal())
    inorder(tree.rightChild)

def postorder(tree):
    """Postorder traversal"""
    if not tree:
        return None
    postorder(tree.leftChild)
    postorder(tree.rightChild)
    print(tree.getRootVal())

def main():
    tree = buildtree()
    print(preorder(tree))
    print(postorder(tree))
    print(inorder(tree))

main()



        
