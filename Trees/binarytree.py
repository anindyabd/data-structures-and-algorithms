from stack import Stack 
import operator

class BinaryTree:
    """A binary tree that uses nodes and references.
    This is just a regular binary tree, not a binary search tree."""

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

def buildParseTree(fpexp):
    """Builds a parse tree, given an 
    expression. Here the operators and operands
    of the expression must all be separated by spaces."""
    fplist = fpexp.split()
    pStack = Stack() #stack that will hold the parent nodes
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(': #insert a left child and move the pointer there (push parent into stack so that you can return)
            currentTree.insertLeft('') 
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i.isdigit(): #store the number and move to the parent (by popping parent off stack)
            currentTree.setRootVal(int(i)) 
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']: #store the operator, move to right child
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')': #move up to parent
            parent = pStack.pop()
            currentTree = parent
        else:
            raise ValueError
    return eTree

pTree = buildParseTree("( 3 + ( 4 * 5 )")

def evaluateParseTree(ptree):
    ops = {'+': operator.add, '-': operator.sub, 
            '*': operator.mul, '/': operator.truediv}
    if ptree == None:
        return None
    elif ptree.getLeftChild() == None and ptree.getRightChild() == None:
        return ptree.getRootVal()
    elif ptree.getRootVal() in ops:
        return ops[ptree.getRootVal()](evaluateParseTree(ptree.getLeftChild()), 
                    evaluateParseTree(ptree.getRightChild()))
    else:
        return None

print(evaluateParseTree(pTree))








        
