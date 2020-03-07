print("Bubble Sort")
# BUBBLE SORT
tab = [10, 2, 7, 6, 8, 4, -2, 3]
def bubble_sort(data):
    for i in range(len(tab)):
        for j in range(len(tab)-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
                print(tab)
bubble_sort(tab)

print("\n", "Merge Sort")
# MERGE SORT
tab2 = [10, 2, 7, 6, 8, 4, 2, 3]

def sort_merge(data):
    if len(data) <= 1:
        return data
    middle = int(len(data) / 2)
    left, right = sort_merge(data[middle:]), sort_merge(data[:middle])
    return merge(left, right)

def merge(left, right):

    leftindex = rightindex = 0
    results = []
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            results.append(left[leftindex])
            leftindex += 1
        else:
            results.append(right[rightindex])
            rightindex += 1
    results.extend(left[leftindex:])
    results.extend(right[rightindex:])
    return results

print(sort_merge(tab2))

print("\n", "Bucket Sort 1")
# BUCKET SORT
tab2= [1, -2, 3]
def bucket_sort(data):
    maxvalue = 0
    minvalue = min(data)
    if minvalue < 0:
        data = [x - minvalue for x in data]
    bucket = []  # secondary list
    results = []  # main result list
    for i in range(len(data)):
        if data[i] > maxvalue:
            maxvalue = data[i]

    for j in range(maxvalue+1):
        bucket.append(0)

    for k in range(len(data)):
        bucket[data[k]] += 1

    for l in range(maxvalue+1):
        if bucket[l] != 0:
            for i in range(1, bucket[l]+1):
                results.append(l)

    if minvalue < 0:
        results = [x + minvalue for x in results]
    return results

print(bucket_sort(tab2))
print("\n", "Bucket Sort 2")
# BUCKET SORT 2
# https://www.programiz.com/dsa/bucket-sort

def bucketSort(array):
    bucket = []

    for i in range(len(array)):
        bucket.append([])

    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


array = [.28, 0.55, .30, .47, .45, .51]
print("Sorted Array in descending order is")
print(bucketSort(array))

# INSERTION SORT
print("\n", "Insertion sort")
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key

    return arr

arr = [12, 11, 14, -1]

print(insertionSort(arr))
print("\n", "Selection Sort")

# SELECTION SORT

def selectionSort(arr):
    for i in range(len(arr)):
        minvalue = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minvalue]:
                minvalue = j
        arr[minvalue], arr[i] = arr[i], arr[minvalue]
    return arr

arr2 = [5, -5, 9, -2, 6]
print(selectionSort(arr2))



