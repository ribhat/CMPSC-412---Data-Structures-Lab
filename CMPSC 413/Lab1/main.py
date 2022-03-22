# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import time

def gcd(a, b):
    smaller =min(a,b)
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            largest_factor = i
    return largest_factor

def find_max(list1):
    max_val = list1[0]
    for item in list1:
        if item > max_val:
            max_val = item
    return max_val

def find_min(list1):
    min_val = list1[0]
    for item in list1:
        if item < min_val:
            min_val = item
    return min_val


def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startTime = time.time()
    print(gcd(135632, 78326))
    executionTime = (time.time() - startTime)
    print('Execution time for gcd in seconds: ' + str(executionTime))

    list2 = []
    list3 = []

    for i in range(1000):
        list2.append(random.randint(1, 1000))

    for i in range(10000):
        list3.append(random.randint(1, 1000))

    startTime = time.time()
    print(find_min(list2))
    executionTime = (time.time() - startTime)
    print('Execution time for find_min for 1,000 elems in seconds: ' + str(executionTime))

    startTime = time.time()
    print(find_min(list3))
    executionTime = (time.time() - startTime)
    print('Execution time for find_min for 10,000 elems in seconds: ' + str(executionTime))

    startTime = time.time()
    print(find_max(list2))
    executionTime = (time.time() - startTime)
    print('Execution time for find_min for 1,000 elems in seconds: ' + str(executionTime))

    startTime = time.time()
    print(find_max(list3))
    executionTime = (time.time() - startTime)
    print('Execution time for find_min for 10,000 elems in seconds: ' + str(executionTime))

    startTime = time.time()
    mergeSort(list2)
    print(list2[0])
    executionTime = (time.time() - startTime)
    print('Execution time for finding min for 1,000 elems using DAC in seconds: ' + str(executionTime))

    startTime = time.time()
    mergeSort(list2)
    print(list2[-1])
    executionTime = (time.time() - startTime)
    print('Execution time for finding max for 10,000 elems using DAC in seconds: ' + str(executionTime))

    startTime = time.time()
    mergeSort(list3)
    print(list3[0])
    executionTime = (time.time() - startTime)
    print('Execution time for finding min for 1,000 elems using DAC in seconds: ' + str(executionTime))

    startTime = time.time()
    mergeSort(list3)
    print(list3[-1])
    executionTime = (time.time() - startTime)
    print('Execution time for finding max for 10,000 elems using DAC in seconds: ' + str(executionTime))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
