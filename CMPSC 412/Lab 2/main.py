# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Vector:

    def __init__(self, capacity = 2):
        self.values = self._create_array(capacity)
        self.capacity = capacity
        self.num_vals = 0

    def __len__(self):
        return self.num_vals

    def __contains__(self, item):
        return item in self.values

    def __getitem__(self, idx):
        if idx > len(self.values) - 1 or idx < - len(self.values): #allows negative indx
            return IndexError("idx out of range")
        return self.values[idx]

    def __setitem__(self, idx, value): #implement resizing
        if idx == self.num_vals:
            self._resize(self.capacity * 2)
            self.values[self.num_vals] = value
            self.num_vals += 1
            return



        if idx > len(self.values) - 1 or idx < 0:
            return IndexError("idx out of range")


        self.values[idx] = value



    def append(self, value):
        if self.num_vals == self.capacity:
            self._resize(self.capacity * 2)
        self.values[self.num_vals] = value
        self.num_vals += 1


    def insert(self, idx, value):
        if idx < 0 or idx > self.num_vals: #cant be past the last elem in our list even if the capacity allows it
            return IndexError("idx out of range")

        #resize if necessary
        if self.num_vals == self.capacity:
            self._resize(2 * self.capacity)

        #move all other elements one position down

        for i in range(self.num_vals - 1, idx - 1, -1): #iterate from back of list and move those elems one unit down
            self.values[i+1] = self.values[i]

        self.values[idx] = value
        self.num_vals += 1

    def remove(self, idx):
        if self.num_vals == 0:
            print("Vector is empty. No item to remove")
            return

        if idx < 0 or idx > self.num_vals - 1:
            return IndexError("idx out of range")

        #if removing last elem
        if idx == self.num_vals:
            self.values[idx] = None
            self.num_vals -= 1
            return

        for i in range(idx, self.num_vals - 1):
            self.values[i] = self.values[i+1]

        #now that all elements are pushed up, need to make the last elem None
        self.values[self.num_vals - 1] = None
        self.num_vals -= 1

    def indexOf(self, item):
        if item not in self.values:
            print("Item not found in list")
            return

        for i in range(self.num_vals):
            if self.values[i] == item:
                return i

    def extend(self, VectorB):
        total_size_needed = self.num_vals + VectorB.num_vals

        while total_size_needed > self.capacity:
            self._resize(2 * self.capacity)

        for i in range(VectorB.num_vals):
            self.values[self.num_vals + i] = VectorB.values[i]
            self.num_vals += 1

    def subvector(self, start, end):
        if start < 0 or end > self.num_vals - 1:
            return IndexError("either start or end out of bounds")

        return self.values[start:end]


    def _create_array(self, size):
        return [None] * size

    def _resize(self, new_capacity):
        new_list = self._create_array(new_capacity)

        for i in range(self.num_vals):
            new_list[i] = self.values[i]

        self.values = new_list
        self.capacity = new_capacity




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    v1 = Vector()
    v2 = Vector()
    v1.append(3)
    v1.append(6)
    v1.append(4)
    v2.append(25)
    v1.extend(v2)
    print("length: ", v1.__len__())
    print("searching for elem 3", v1.__contains__(3))
    print("getting item at index 1", v1.__getitem__(1))
    v1.__setitem__(0, 100)
    print("set item at index 0 to 100", v1.__getitem__(0))
    v1.append(150)
    print("Appending value 150 to end of vector. index of 150 is now: ", v1.indexOf(150))
    v1.insert(1, 20)
    print("Insert value 20 into index 1. Values at index 1 and 2 are now: ", v1.__getitem__(1), v1.__getitem__(2))
    v1.remove(1)
    print("Removed value 20 from vector. Item in index 1 is now: ", v1.__getitem__(1))
    print("Index of value 25: ", v1.indexOf(25))
    print("Subvector from index 0 to 2: ", v1.subvector(0, 2))





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
