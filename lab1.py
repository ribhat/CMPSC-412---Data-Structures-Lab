# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import time

def generate_random_nums(n):
    # Use a breakpoint in the code line below to debug your script.
    list1 = []
    for i in range(n):
        list1.append(random.randint(1, 10000))
    return list1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list1 = generate_random_nums(10000)
    dict1 = {}

    count = 0
    for item in list1:
        dict1[count] = item
        count = count + 1

    #Comparing Print Statements
    startTime = time.time()
    print(list1)
    executionTime = (time.time() - startTime)
    print('Execution time for print list in seconds: ' + str(executionTime))

    startTime = time.time()
    print(dict1.values())
    executionTime = (time.time() - startTime)
    print('Execution time for print dict in seconds: ' + str(executionTime))

    #Comparing Retrieval Times
    rand_num = random.randint(1, 10000)
    startTime = time.time()
    print(rand_num in list1)
    executionTime = (time.time() - startTime)
    print('Execution time for retrieval from list in seconds: ' + str(executionTime))

    startTime = time.time()
    print(rand_num in dict1.values())
    executionTime = (time.time() - startTime)
    print('Execution time for retrieval from dict in seconds: ' + str(executionTime))

    #Comparison for Insert and Print
    rand_num2 = random.randint(1, 10000)
    startTime = time.time()
    list1.append(rand_num2)
    print(list1)
    executionTime = (time.time() - startTime)
    print('Execution time for insert and print from list in seconds: ' + str(executionTime))

    startTime = time.time()
    dict1[count] = rand_num2
    print(dict1.keys())
    executionTime = (time.time() - startTime)
    print('Execution time for insert and print from dict in seconds: ' + str(executionTime))


    #Comparison of Delete
    rand_num3 = random.randint(1, 10000)
    startTime = time.time()
    list1.remove(rand_num3)
    executionTime = (time.time() - startTime)
    print('Execution time for delete from list in seconds: ' + str(executionTime))

    startTime = time.time()
    for key, value in dict1.items():
        if value == rand_num3:
            del dict1[key]
            break
    executionTime = (time.time() - startTime)
    print('Execution time for delete from dict in seconds: ' + str(executionTime))





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
