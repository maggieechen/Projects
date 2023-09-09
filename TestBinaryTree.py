
#  File: TestBinaryTree.py

#  Description: This program adds helper methods that can be tested in the Tree class. It will create several trees and show that the methods work.

import sys

class Node (object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1

    def get_level_helper(self,level):
        left_level_list = []
        right_level_list = []
        level_list = []
        if self == None or level >= self.get_height():
            level_list = left_level_list + right_level_list
            return level_list
        if level == 0:
            level_list.append(self)
            return level_list
        if level >= 1:
            if self.lChild is not None:
                left_level_list = self.lChild.get_level_helper(level - 1)
            if self.rChild is not None:
                right_level_list = self.rChild.get_level_helper(level - 1)
            level_list = left_level_list + right_level_list
        return level_list

    def left_view_helper(self):
        level = self.get_height()
        left_view_list = []
        for x in range(0,level):
            val = self.get_level_helper(x)
            if len(val) > 0:
                left_view_list.append(val[0].data)
        return left_view_list

    def sum_leaf_helper(self):
        left_sum = 0
        right_sum = 0
        if self.lChild == None and self.rChild == None:
            return self.data
        else:
            if self.lChild is not None:
                left_sum = self.lChild.sum_leaf_helper()
            if self.rChild is not None:
                right_sum = self.rChild.sum_leaf_helper()
        return left_sum + right_sum
            
    
class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        if self.root is not None:
            self.root.print_node(level)

    def get_height(self):
        if self.root is not None:
            return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    def minimum(self):
        current = self.root
        parent = current
        while current != None:
            parent = current
            current = current.lChild
        return parent

    def maximum(self):
        current = self.root
        parent = current
        while current != None:
            parent = current
            current = current.rChild
        return parent
    
    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        if self.root is None:
            return None
        elif self.root.lChild == None and self.root.rChild == None:
            return 0
        else:
            return self.maximum().data - self.minimum().data

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        if self.root is not None:
            return self.root.get_level_helper(level)
        else:
            return []

    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        if self.root is not None:
            return self.root.left_view_helper()
        else:
            return []
        

    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        if self.root is not None:
            return self.root.sum_leaf_helper()
    
def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescope will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())
    #print("Level:",t1.get_level(3))
    print("Tree range is:",t1.range())
    print("Tree left side view is:",t1.left_side_view())
    print("Sum of leaf nodes is:",t1.sum_leaf_nodes())
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())
    #print("Level:",t1.get_level(0))
    print("Tree range is:",t2.range())
    print("Tree left side view is:",t2.left_side_view())
    print("Sum of leaf nodes is:",t2.sum_leaf_nodes())
    print("##########################")
# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())
    #print("Level:",t1.get_level(1))
    print("Tree range is:",t3.range())
    print("Tree left side view is:",t3.left_side_view())
    print("Sum of leaf nodes is:",t3.sum_leaf_nodes())
    print("##########################")
    
if __name__ == "__main__":
    main()



