# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import random
import time
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def countingSort(arr): #used for smaller range of values (sort in O(n))
    max_val = max(arr)
    new_list = [0] * (max_val + 1)
    if len(arr) == 0 or len(arr) == 1:
        return arr

    for i in range(len(arr)):
        new_list[arr[i]] += 1 #generates frequency array

    for i in range(len(new_list)):
        if i == 0:
            new_list[i] = new_list[i] #no change for first value
            continue
        new_list[i] = new_list[i] + new_list[i-1]

    prev_max = new_list[0]
    arr_indx = 0
    for i in range(1, len(new_list)):
        if new_list[i] > prev_max:
            if new_list[i] - prev_max > 1:
                difference = new_list[i] - prev_max
                prev_max = new_list[i]
                for j in range(arr_indx, difference + arr_indx): #if a number appears more than once, copy it into original array that many times
                    arr[j] = i
                    arr_indx += 1
            else:
                arr[arr_indx] = i
                arr_indx += 1
                prev_max = new_list[i]
        if arr_indx > len(arr):
            break

    return arr





def sort_data(list1, func, low = None, high = None ):


    if func == quickSort:
        if low == None or high == None:
            print("Error, please enter low, high values for quicksort")
            return
        #startTime = time.time()
        startTime = datetime.datetime.now()
        func(list1, low, high)
        executionTime = (datetime.datetime.now() - startTime)
        #executionTime = (time.time() - startTime)
        print('Execution time for sort ' + str(len(list1)) + ' students using ' + str(func.__name__) + ': ' + str(executionTime.total_seconds() * 1000) + ' ms') #to see miliseconds
    elif func == countingSort:
        startTime = datetime.datetime.now()
        func(list1)
        executionTime = (datetime.datetime.now() - startTime)
        # executionTime = (time.time() - startTime)
        print('Execution time for sort ' + str(len(list1)) + ' students using ' + str(func.__name__) + ': ' + str(executionTime.total_seconds() * 1000) + ' ms')

    else:
        #startTime = time.time()
        startTime = datetime.datetime.now()
        func(list1)
        executionTime = (datetime.datetime.now() - startTime)
        #executionTime = (time.time() - startTime)
        print('Execution time for sort ' + str(len(list1)) + ' students using ' + str(func.__name__) + ': ' + str(executionTime.total_seconds() * 1000) + ' ms')


def generate_numbers(num, low = 0, high = 10000):
    list1 = []
    for i in range(num):
        list1.append(random.randint(low, high))
    return list1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list1 = generate_numbers(100)
    sort_data(list1, mergeSort)
    sort_data(list1, quickSort,0 , len(list1) - 1)
    sort_data(list1, countingSort)

    list2 = generate_numbers(500)
    sort_data(list2, mergeSort)
    sort_data(list2, quickSort, 0, len(list2) - 1)
    sort_data(list2, countingSort)

    list3 = generate_numbers(900)
    sort_data(list3, mergeSort)
    sort_data(list3, quickSort, 0, len(list3) - 1)
    sort_data(list3, countingSort)

    list4 = generate_numbers(100000)
    sort_data(list4, mergeSort)
    #sort_data(list3, quickSort, 0, len(list3) - 1)
    sort_data(list4, countingSort)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
