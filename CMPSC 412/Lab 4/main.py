# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import datetime
import sys

merge_memory = 0
quicksort_memory = 0
binarysearch_memory = 0

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def guess_num(low, high):
    guessed = False
    print("Lets go")
    count = 1

    while not guessed:
        guess_value = (low + high) // 2
        input_val = input("Is " + str(guess_value) + " the value you were thinking of? (H = guess was too high, L = guess was too low, Y= yes): ")
        if low > high:
            print("Value being searched for is not in specified range given at start")
            break

        if input_val == 'y' or input_val == 'Y':
            print("Yay, we were able to locate your value in " + str(count) + ' tries')
            guessed = True
        if input_val == 'h' or input_val == 'H':
            high = guess_value - 1
        if input_val == 'l' or input_val == 'L':
            low = guess_value + 1

        count += 1

    print("size of count, guess_val used for this program: " + str(count.__sizeof__()) + ' bytes, ' + str(guess_value.__sizeof__()) + ' bytes')





def insertionSort(arr):
    #print("Memory needed for insertionSort: " + str(sys.getsizeof(arr)))
    for i in range(0, len(arr) - 1):
        key = arr[i+1]

        j = i

        while key < arr[j] and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    total_memory = int(sys.getsizeof(arr)) + int(sys.getsizeof(i)) + int(sys.getsizeof(j))
    return total_memory


def selectionSort(arr):
    #print("Memory needed for selectionSort: " + str(sys.getsizeof(arr)))
    for i in range(len(arr)):
        min_indx = i

        for j in range(i+1, len(arr)):
            if arr[min_indx] > arr[j]:
                min_indx = j

        arr[i], arr[min_indx] = arr[min_indx], arr[i] #swap values

    total_memory = int(sys.getsizeof(arr)) + int(sys.getsizeof(i)) + int(sys.getsizeof(j))
    return total_memory




def bubbleSort(arr):
    #print("Memory needed for bubbleSort: " + str(sys.getsizeof(arr)))
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        for j in range(0, n - i - 1): #search through i+1 elems from the back
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #swap values

    total_memory = int(sys.getsizeof(arr)) + int(sys.getsizeof(i)) + int(sys.getsizeof(j))
    return total_memory




def mergeSort(arr):
    global merge_memory
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        merge_memory += int(sys.getsizeof(L)) + int(sys.getsizeof(R))

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

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    total_mem = int(sys.getsizeof(arr)) + int(sys.getsizeof(low)) + int(sys.getsizeof(high)) + int(sys.getsizeof(j)) + int(sys.getsizeof(i))
    return (i + 1), total_mem


def quickSort(arr, low, high):
    #print("Memory needed for quickSort: " + str(sys.getsizeof(arr)))
    mem = 0
    if len(arr) == 1:
        return
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi, mem = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    total_mem = int(sys.getsizeof(arr)) + int(sys.getsizeof(low)) + int(sys.getsizeof(high)) + mem
    return total_mem

def linear_search(arr, target):
    #print("Memory needed for linearSeach: " + str(sys.getsizeof(arr)))
    for i in range(len(arr)):
        if arr[i] == target:
            print("Index of value " + str(target) + " is: " + str(i))
            return i
    print("target not found")
    total_mem = int(sys.getsizeof(arr)) + int(sys.getsizeof(target)) + int(sys.getsizeof(i))
    return total_mem

def binary_search(arr, low, high, target):
    #print("Memory needed for binarySearch: " + str(sys.getsizeof(arr)))
    found = False

    if high < low:
        return -1
    else:
        mid = (high + low) // 2

        if arr[mid] == target:
            print("Value " + str(target) + " is at index: " + str(mid))
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid-1, target)
        else:
            return binary_search(arr, mid+1, high, target)
    binarysearch_memory = int(sys.getsizeof(arr)) + int(sys.getsizeof(target)) + int(sys.getsizeof(low)) + int(sys.getsizeof(high))


def read_data_by_id(file):
    dict1 = {}
    with open(file) as f:
        lines = f.readlines()

    for line in lines:
        split_words = line.split(" ")

        if split_words[0] not in dict1.keys():
            dict1[int(split_words[0])] = split_words

    return dict1

def read_data_by_firstname(file):
    dict1 = {}
    with open(file) as f:
        lines = f.readlines()

    for line in lines:
        split_words = line.split(" ")

        if split_words[1] not in dict1.keys():
            dict1[str(split_words[1])] = split_words

    return dict1

def sort_data_by_id(file, func, target = None, low = None, high = None):
    student_data_dict = read_data_by_id(file)

    #make list of dictionary keys
    student_id_list = list(student_data_dict.keys())

    if func == linear_search:
        #startTime = time.time()
        startTime = datetime.datetime.now()
        func(student_id_list, target)
        executionTime = (datetime.datetime.now() - startTime)
        #executionTime = (time.time() - startTime)
        print('Execution time for search students using ' + str(func.__name__) + ': ' + str(executionTime.total_seconds() * 1000)) #to see miliseconds

    elif func == quickSort:
        # if low == None and high == None:
        #     print("Error, please enter low, high values for quicksort")
        #     return
        # if high == None:
        #     high = len(student_id_list) - 1
        #startTime = time.time()
        startTime = datetime.datetime.now()
        size = func(student_id_list, 0, len(student_id_list) - 1)
        f = open("new_file_by_id.txt", "w")
        for id in student_id_list:
            f.write(str(student_data_dict.get(id)))
            f.write("\n")
        executionTime = (datetime.datetime.now() - startTime)
        #executionTime = (time.time() - startTime)
        print('Execution time for sort ' + str(len(student_id_list)) + ' students using ' + str(func.__name__) + ': ' + str(executionTime.total_seconds() * 1000) + ' ms') #to see miliseconds
        print("Space actually used: " + str(size))

    elif func  == mergeSort:
        startTime = datetime.datetime.now()
        size = func(student_id_list)  # returns memory used
        f = open("new_file_by_id.txt", "w")
        for id in student_id_list:
            f.write(str(student_data_dict.get(id)))
            f.write("\n")
        executionTime = (datetime.datetime.now() - startTime)
        # executionTime = (time.time() - startTime)
        print('Execution time for sort students by id using ' + str(func.__name__) + ': ' + str(
            executionTime.total_seconds() * 1000))
        # print('Mimimum space needed: ' + str(sys.getsizeof(student_id_list)))
        print("Space actually used: " + str(merge_memory))

    else:
        #startTime = time.time()
        startTime = datetime.datetime.now()
        size = func(student_id_list) #returns memory used
        f = open("new_file_by_id.txt", "w")
        for id in student_id_list:
            f.write(str(student_data_dict.get(id)))
            f.write("\n")
        executionTime = (datetime.datetime.now() - startTime)
        #executionTime = (time.time() - startTime)
        print('Execution time for sort students by id using ' + str(func.__name__) + ': ' + str(executionTime.total_seconds() * 1000))
        #print('Mimimum space needed: ' + str(sys.getsizeof(student_id_list)))
        print("Space actually used: " + str(size))

def sort_data_by_firstname(file, func, target=None, low = None, high = None):
    student_data_dict = read_data_by_firstname(file)

    # make list of dictionary keys
    student_firstname_list = list(student_data_dict.keys())

    if func == linear_search:
        # startTime = time.time()
        startTime = datetime.datetime.now()
        func(student_firstname_list, target)
        executionTime = (datetime.datetime.now() - startTime)
        # executionTime = (time.time() - startTime)
        print('Execution time for search students by first name using ' + str(func.__name__) + ': ' + str(
            executionTime.total_seconds() * 1000))  # to see miliseconds
    elif func == quickSort:
        # if low == None or high == None:
        #     print("Error, please enter low, high values for quicksort")
        #     return
        #startTime = time.time()
        startTime = datetime.datetime.now()
        size = func(student_firstname_list, 0, len(student_firstname_list) - 1)
        f = open("new_file_by_fn.txt", "w")
        for fn in student_firstname_list:
            f.write(str(student_data_dict.get(fn)))
            f.write("\n")
        executionTime = (datetime.datetime.now() - startTime)
        #executionTime = (time.time() - startTime)
        print('Execution time for sort ' + str(len(student_firstname_list)) + ' students using ' + str(func.__name__) + ': ' + str(executionTime.total_seconds() * 1000) + ' ms') #to see miliseconds
        print("Space actually used: " + str(size))
    elif func  == mergeSort:
        startTime = datetime.datetime.now()
        size = func(student_firstname_list)  # returns memory used
        f = open("new_file_by_fn.txt", "w")
        for id in student_firstname_list:
            f.write(str(student_data_dict.get(id)))
            f.write("\n")
        executionTime = (datetime.datetime.now() - startTime)
        # executionTime = (time.time() - startTime)
        print('Execution time for sort students by id using ' + str(func.__name__) + ': ' + str(
            executionTime.total_seconds() * 1000))
        # print('Mimimum space needed: ' + str(sys.getsizeof(student_id_list)))
        print("Space actually used: " + str(merge_memory))

    else:
        # startTime = time.time()
        startTime = datetime.datetime.now()
        size = func(student_firstname_list)
        f = open("new_file_by_fn.txt", "w")
        for fn in student_firstname_list:
            f.write(str(student_data_dict.get(fn)))
            f.write("\n")
        executionTime = (datetime.datetime.now() - startTime)
        # executionTime = (time.time() - startTime)
        print('Execution time for sort students by first name using ' + str(func.__name__) + ': ' + str(
            executionTime.total_seconds() * 1000))
        print("Space actually used: " + str(size))

    # for id in student_id_list:
    #     print(student_data_dict.get(id))







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('')

    sort_data_by_id("student_database.txt", linear_search, 5597)
    sort_data_by_id("student_database.txt", selectionSort)
    sort_data_by_id("student_database.txt", insertionSort)
    sort_data_by_id("student_database.txt", bubbleSort)
    sort_data_by_id("student_database.txt", mergeSort)
    sort_data_by_id("student_database.txt", quickSort)

    print('')

    sort_data_by_firstname("student_database.txt", linear_search, 9999)
    sort_data_by_firstname("student_database.txt", selectionSort)
    sort_data_by_firstname("student_database.txt", insertionSort)
    sort_data_by_firstname("student_database.txt", bubbleSort)
    sort_data_by_firstname("student_database.txt", mergeSort)
    sort_data_by_firstname("student_database.txt", quickSort)


    print('')
    #
    # guess_num(1, 10000)











# See PyCharm help at https://www.jetbrains.com/help/pycharm/
