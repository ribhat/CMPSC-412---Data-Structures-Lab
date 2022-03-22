# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# https://gist.github.com/samidhtalsania/6659380
# https://gist.github.com/zjplab/b052af68196bec5ce48dcc39b0acef2f


class Node():

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class Tree():

    def __init__(self):
        self.root = None
        self.size = 0
        self.added_nodes = []

    def add_node(self, key, node=None):

        if node is None:
            node = self.root #if no node specified, set to root

        if self.root is None:
            self.root = Node(key)
            self.size += 1
            self.added_nodes.append(key)

        else:

            if key <= node.key:
                if node.left is None:
                    node.left = Node(key)
                    node.left.parent = node
                    self.size += 1
                    self.added_nodes.append(key)
                    return
                else:
                    return self.add_node(key, node=node.left) #recursively call on left node
            else:
                if node.right is None:
                    node.right = Node(key)
                    node.right.parent = node
                    self.size += 1
                    self.added_nodes.append(key)
                    return
                else:
                    return self.add_node(key, node=node.right)

    def search(self, key, node=None):

        if node is None:
            node = self.root

        if self.root.key == key:
            return self.root

        else:
            if node.key == key:
                return node

            elif key < node.key and node.left is not None:
                return self.search(key, node=node.left)
            elif key > node.key and node.right is not None:
                return self.search(key, node=node.right)

            else:
                print("key does not exist")
                return None

    def delete_node(self, key, node=None):
        # search for the node to be deleted in tree
        if node is None:
            node = self.search(key)

        # root has no parent node
        if self.root.key == node.key:  # if it is root
            parent_node = self.root
        else:
            parent_node = node.parent

        '''case 1: The node has no chidren'''
        if node.left is None and node.right is None:
            if key <= parent_node.key:
                parent_node.left = None
                self.size -= 1
                self.added_nodes.remove(key)
            else:
                parent_node.right = None
                self.size -= 1
                self.added_nodes.remove(key)
            return

        '''case 2: The node has children'''
        ''' if it has a single left node'''
        if node.left is not None and node.right is None:
            if node.left.key < parent_node.key:
                parent_node.left = node.left
                self.size -= 1
                self.added_nodes.remove(key)
            else:
                parent_node.right = node.left
                self.size -= 1
                self.added_nodes.remove(key)

            return

        '''if it has a single right node'''
        if node.right is not None and node.left is None:
            if node.key <= parent_node.key:
                parent_node.left = node.right
                self.size -= 1
                self.added_nodes.remove(key)
            else:
                parent_node.right = node.right
                self.size -= 1
                self.added_nodes.remove(key)
            return

        '''if it has two children'''
        '''find the node with the minimum value from the right subtree.
           copy its value to thhe node which needs to be removed.
           right subtree now has a duplicate and so remove it.'''
        if node.left is not None and node.right is not None:
            min_value = self.find_minimum(node)
            node.key = min_value.key
            min_value.parent.left = None
            self.size -= 1
            self.added_nodes.remove(key)
            return

    def find_minimum(self, node=None):

        if node is None:
            node = self.root

        '''find mimimum value from the right subtree'''

        '''case when there is only a root node'''
        if node.right is not None:
            node = node.right
        else:
            return node

        if node.left is not None:
            return self.find_minimum(node=node.left)
        else:
            return node

    def return_minimum(self, node = None):
        if node is None:
            node = self.root
        while node.left is not None:
            node = node.left
        return node.key

    def return_maximum(self, node = None):
        if node is None:
            node = self.root
        while node.right is not None:
            node = node.right
        return node.key
    def all_nodes(self):
        return self.added_nodes


    def in_order(self, node = -1):
        if node == -1:
            node = self.root
        if node:
            #print("Node.left is: " + str(node.left))
            self.in_order(node.left)
            print(node.key)
            self.in_order(node.right)

    def pre_order(self, node = -1):
        if node == -1:
            node = self.root
        if node:
            #print("Node.left is: " + str(node.left))

            self.pre_order(node.left)
            self.pre_order(node.right)
            print(node.key)

    def post_order(self, node = -1):
        if node == -1:
            node = self.root
        if node:
            #print("Node.left is: " + str(node.left))
            self.in_order(node.left)
            self.in_order(node.right)
            print(node.key)

    def merge_trees(self, t2):
        for node in t2.all_nodes():
            self.add_node(node)







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    t = Tree()
    t.add_node(5)
    t.add_node(3)
    t.add_node(7)
    t.add_node(4)
    t.add_node(27)
    t.add_node(1)
    t.add_node(100)
    t.add_node(29)
    t.add_node(300)
    t.delete_node(100)
    print(t.all_nodes())

    tt = Tree()
    tt.add_node(10)
    tt.add_node(9)
    tt.add_node(11)
    tt.add_node(8)
    tt.delete_node(8)
    print(tt.all_nodes())

    t.merge_trees(tt)
    print(t.all_nodes())

    print("In order traversal is: ")
    t.in_order()
    #print("\n")
    print("Pre order traversal is: ")
    t.pre_order()
    #print("\n")
    print("Post order traversal is: ")
    t.post_order()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
