# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#Python list functions as a stack

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def reverse_str(str):
    stack1 = Stack()
    list1 = []

    for char in str:
        stack1.push(char)

    while stack1.isEmpty() == False:
        list1.append(stack1.pop())

    return list1


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enQueue(self, x):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        self.stack1.append(x)

        while len(self.stack2) != 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()

    def deQueue(self):
        if len(self.stack1) == 0:
            print("Q is Empty")

        x = self.stack1[-1]
        self.stack1.pop()
        return x

def isValid(s: str) -> bool:

    list1 = []

    for char in s:
        if char == "{" or char == '[' or char == '(':
            list1.append(char)

        if char == "}":
            if len(list1) == 0:
                return False
            if list1.pop() != '{':
                return False
        if char == "]":
            if len(list1) == 0:
                return False
            if list1.pop() != '[':
                return False
        if char == ")":
            if len(list1) == 0:
                return False
            if list1.pop() != '(':
                return False
    return len(list1) == 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Number 1: ")
    output = reverse_str("Madam")
    print('Madam reversed: ', output)
    output = reverse_str("racecar")
    print('racecar reversed: ', output)
    output = reverse_str("MadamImAdam")
    print('Madam Im Adam reversed: ', output)
    print('')

    print("Number 2: ")
    print('Queue using two stacks: ')
    print('enqueue 1, 2, 3. Then dequeue twice')

    q = Queue()

    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    print(q.deQueue())
    print(q.deQueue())
    print('')

    print("Number 3: ")
    output = isValid("{{(}}")
    print('Is {{(}} is balanced:  ', output)

    output = isValid("{{()}}")
    print('Is {{()}} is balanced:  ', output)

    output = isValid("{{(w)}}")
    print('Is {{(w)}} is balanced:  ', output)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
