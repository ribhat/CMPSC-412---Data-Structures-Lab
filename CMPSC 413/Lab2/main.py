# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import datetime

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def guess_num(low, high):
    guessed = False
    print("Lets go")

    while not guessed:
        guess_value = (low + high) // 2
        input_val = input("Is " + str(guess_value) + " the value you were thinking of? (H = guess was too high, L = guess was too low, Y= yes")
        if low >= high:
            guessed = True

        if input_val == 'y' or input_val == 'Y':
            guessed = True
            return guess_value
        if input_val == 'h' or input_val == 'H':
            high = guess_value - 1
        if input_val == 'l' or input_val == 'L':
            low = guess_value + 1

    print("Value being searched for is not in specified range given at start")


def insertionSort(arr):
    for i in range(0, len(arr) - 1):
        key = arr[i+1]

        j = i

        while key < arr[j] and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def selectionSort(arr):
    for i in range(len(arr)):
        min_indx = i

        for j in range(i+1, len(arr)):
            if arr[min_indx] > arr[j]:
                min_indx = j

        arr[i], arr[min_indx] = arr[min_indx], arr[i] #swap values


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        for j in range(0, n - i - 1): #search through i+1 elems from the back
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #swap values

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

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print("Index of value " + str(target) + " is: " + str(i))
            return i
    print("target not found")
    return None

def binary_search(arr, low, high, target):
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


def read_data(file):
    dict1 = {}
    with open(file) as f:
        lines = f.readlines()

    for line in lines:
        split_words = line.split(" ")

        if split_words[0] not in dict1.keys():
            dict1[int(split_words[0])] = split_words

    return dict1

def sort_data(file, func, target = None):
    student_data_dict = read_data(file)

    #make list of dictionary keys
    student_id_list = list(student_data_dict.keys())

    if func == linear_search:
        #startTime = time.time()
        startTime = datetime.datetime.now()
        func(student_id_list, target)
        executionTime = (datetime.datetime.now() - startTime)
        #executionTime = (time.time() - startTime)
        print('Execution time for search students using ' + str(func.__name__) + ': ' + str(executionTime.total_seconds() * 1000)) #to see miliseconds
    else:
        #startTime = time.time()
        startTime = datetime.datetime.now()
        func(student_id_list)
        executionTime = (datetime.datetime.now() - startTime)
        #executionTime = (time.time() - startTime)
        print('Execution time for sort students using ' + str(func.__name__) + ': ' + str(executionTime.total_seconds() * 1000))

    # for id in student_id_list:
    #     print(student_data_dict.get(id))







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list1 = [4,2,6,8]
    print(list1)

    print("Linear Search: ")
    linear_search(list1, 2)
    print("Binary Search: ")
    binary_search(list1, 0, 3, 2)

    best_case = [2, 4, 5, 8, 9, 10, 15, 19, 25, 32]
    worst_case = [9, 8, 5, 4, 2]

    insertionSort(best_case)

    print("Best case sorted with insertion sort: " + str(list1))

    insertionSort((worst_case))




    list2 = [ 4,1,6,3]
    selectionSort(list2)
    print("List 2 sorted with selection sort: " + str(list2))

    print('')

    sort_data("student_database.txt", linear_search, 9999)
    sort_data("student_database.txt", selectionSort)
    sort_data("student_database.txt", insertionSort)
    sort_data("student_database.txt", bubbleSort)
    sort_data("student_database.txt", mergeSort)

    print('')

    sort_data("student_database_sorted.txt", linear_search, 9999)
    sort_data("student_database_sorted.txt", selectionSort)
    sort_data("student_database_sorted.txt", insertionSort)
    sort_data("student_database_sorted.txt", bubbleSort)
    sort_data("student_database_sorted.txt", mergeSort)

    print('')

    sort_data("student_database_same.txt", linear_search, 9999)
    sort_data("student_database_same.txt", selectionSort)
    sort_data("student_database_same.txt", insertionSort)
    sort_data("student_database_same.txt", bubbleSort)
    sort_data("student_database_same.txt", mergeSort)

    print('')

    guess_num(1, 10000)











# See PyCharm help at https://www.jetbrains.com/help/pycharm/
