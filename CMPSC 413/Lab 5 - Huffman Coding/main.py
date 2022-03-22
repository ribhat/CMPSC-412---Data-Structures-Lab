# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import heapq as hq

class PriorityQueueHeap():

    def __init__(self):

        # List of items, flattened max heap. The first element is not used.
        # Each node is a tuple of (value, priority, insert_counter)
        self.nodes = [None]  # first element is not used

        # Current state of the insert counter
        self.insert_counter = 0          # tie breaker, keeps the insertion order

    # Comparison function between two nodes
    # Higher priority wins
    # On equal priority: Lower insert counter wins
    def _is_higher_than(self, a, b):
        return b[1] < a[1] or (a[1] == b[1] and a[2] < b[2])

    def __len__(self):
        return len(self.nodes) - 1

    # Move a node up until the parent is bigger
    def _heapify(self, new_node_index):
        while 1 < new_node_index:
            new_node = self.nodes[new_node_index]
            parent_index = new_node_index // 2
            parent_node = self.nodes[parent_index]

            # Parent too big?
            if self._is_higher_than(parent_node, new_node):
                break

            # Swap with parent
            tmp_node = parent_node
            self.nodes[parent_index] = new_node
            self.nodes[new_node_index] = tmp_node

            # Continue further up
            new_node_index = parent_index

    # Add a new node with a given priority
    def push(self, value, priority):
        new_node_index = len(self.nodes)
        self.insert_counter += 1
        self.nodes.append([value, priority, self.insert_counter])

        # Move the new node up in the hierarchy
        self._heapify(new_node_index)

    # Return the top element
    def peek(self):
        if len(self.nodes) == 1:
            return None
        else:
            return self.nodes[1][0]


    def bubbleDown(self, idx):
        child_idx = idx * 2
        # if no child exists for this index
        if child_idx > len(self.nodes) - 1:
            return

        if child_idx + 1 < len(self.nodes) and self.nodes[child_idx] < self.nodes[child_idx + 1]: #if right child exists and it is bigger we will use that
            child_idx += 1

        if self.nodes[child_idx][1] > self.node[idx][1]: #swap parent and child
            tmp_node = self.nodes[child_idx]
            self.nodes[child_idx] = self.nodes[idx]
            self.nodes[idx] = tmp_node
            self.bubbleDown(child_idx)




    def changePriority(self, value, newPriority):
        if len(self.nodes) == 1:
            return "Queue is empty"

        item_idx = None
        for i in range(1, len(self.nodes)):
            if self.nodes[i][0] == value:
                oldPriority = self.nodes[i][1]
                self.nodes[i][1] = newPriority
                item_idx = i
                break;
            if i == len(self.nodes) - 1:
                return "Item does not exist in queue"

        #priority stays same
        if oldPriority == newPriority:
            return

        # increasing priority
        if newPriority > oldPriority:
            self._heapify(item_idx)

        #decreasing priority
        if newPriority < oldPriority:
            self.bubbleDown(item_idx)

    # Remove the top element and return it
    def pop(self):

        if len(self.nodes) == 1:
            raise LookupError("Heap is empty")

        result = self.nodes[1][0]

        # Move empty space down
        empty_space_index = 1
        while empty_space_index * 2 < len(self.nodes):

            left_child_index = empty_space_index * 2
            right_child_index = empty_space_index * 2 + 1

            # Left child wins
            if (
                len(self.nodes) <= right_child_index # if right child is out of array bounds (does not exist)
                or self._is_higher_than(self.nodes[left_child_index], self.nodes[right_child_index]) # or if left child is > right child
            ):
                self.nodes[empty_space_index] = self.nodes[left_child_index]
                empty_space_index = left_child_index #swap in the left child into the empty space

            # Right child wins
            else:
                self.nodes[empty_space_index] = self.nodes[right_child_index]
                empty_space_index = right_child_index #swap in the right child into the empty space

        # Swap empty space with the last element and heapify
        last_node_index = len(self.nodes) - 1
        self.nodes[empty_space_index] = self.nodes[last_node_index]
        self._heapify(empty_space_index)

        # Throw out the last element because its empty
        self.nodes.pop()

        return result

class PriorityQueueNode:

    def __init__(self, value, priority):
        self.data = value
        self.priority = priority
        self.next = None

class PriorityQueueLL:

    def __init__(self):

        self.front = None
        self.size = 0

    # Method to check Priority Queue is Empty
    # or not if Empty then it will return True
    # Otherwise False
    def isEmpty(self):

        if self.front == None:
            return True
        else:
            return False

    # Method to add items in Priority Queue
    # According to their priority value
    def push(self, value, priority):
        if self.isEmpty() == True:
            self.front = PriorityQueueNode(value, priority)
            self.size = 1
            return
        else:
            # if new elem has higher priority
            if self.front.priority > priority:
                newNode = PriorityQueueNode(value, priority)
                # Updating the new node next value
                newNode.next = self.front
                # Assigning it to self.front
                self.front = newNode
                self.size += 1

                return
            else:
                # Traversing through Queue until it
                # finds the next smaller priority node
                temp = self.front
                while temp.next:
                    # If same priority node found then current
                    # node will come after previous node
                    if priority <= temp.next.priority:
                        break

                    temp = temp.next

                newNode = PriorityQueueNode(value, priority)
                newNode.next = temp.next
                temp.next = newNode
                self.size += 1

                return

    def pop(self):

        if self.isEmpty() == True:
            return
        else:
            ans = self.front.data
            self.front = self.front.next
            self.size -= 1
            return ans

    def remove(self, item):
        temp = self.front

        if self.size == 1 and temp.data == item:
            self.front = None
            self.size -= 1
            return 1

        #if first elem is to be removed
        if temp.data == item:
            self.front = self.front.next
            self.size -= 1
            return 1


        #if there are at least 2 elems
        while temp.next != None:
            print("Next.data = " + str(temp.next.data) + " and item = " +  str(item))
            if temp.next.data == item:
                temp.next = temp.next.next
                return 1
            temp = temp.next

        return 0

    def peek(self):
        if self.isEmpty() == True:
            return
        else:
            return self.front.data

    def traverse(self):

        if self.isEmpty() == True:
            print("Queue is Empty!")
            return
        else:
            temp = self.front
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

    def changePriority(self, item, newPriority):
        ans = self.remove(item)
        if ans == 0:
            return "Item does not exist"

        self.push(item, newPriority)


def generateFreqArr(input_str):
    dict1 = {}
    for ch in input_str:
        if ch in dict1.keys():
            dict1[ch] += 1
        else:
            dict1[ch] = 1

    #build min priority queue
    #pq = PriorityQueueLL()
    list2 = []
    for key in dict1.keys():
        list2.append([dict1[key], key])
    hq.heapify(list2)
    print(list2)


path = input("Enter path to file: ")
with open(path) as f:
    textFileAsString = f.read()

def buildTree(pq):
    return




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generateFreqArr('aaabbc')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
