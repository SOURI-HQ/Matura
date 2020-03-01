# # BUBBLE SORT
# tab = [10, 2, 7, 6, 8, 4, -2, 3]
# def bubble_sort(data):
#     for i in range(len(tab)):
#         for j in range(len(tab)-1):
#             if tab[j] > tab[j+1]:
#                 tab[j], tab[j+1] = tab[j+1], tab[j]
#                 print(tab)
# bubble_sort(tab)
#
# # MERGE SORT
# print("\n")
# tab2 = [10, 2, 7, 6, 8, 4, 2, 3]
#
# def sort_merge(data):
#     if len(data) <= 1:
#         return data
#     middle = int(len(data) / 2)
#     left, right = sort_merge(data[middle:]), sort_merge(data[:middle])
#     return merge(left, right)
#
# def merge(left, right):
#
#     leftindex = rightindex = 0
#     results = []
#     while leftindex < len(left) and rightindex < len(right):
#         if left[leftindex] < right[rightindex]:
#             results.append(left[leftindex])
#             leftindex += 1
#         else:
#             results.append(right[rightindex])
#             rightindex += 1
#     results.extend(left[leftindex:])
#     results.extend(right[rightindex:])
#     return results
#
# print(sort_merge(tab2))

# BUCKET SORT
tab2= [1, -2, 3]
def bucket_sort(data):
    maxvalue = 0
    minvalue = min(data)
    if minvalue < 0:
        data = [x - minvalue for x in data]
    result = []
    results = []
    for i in range(len(data)):
        if data[i] > maxvalue:
            maxvalue = data[i]
    for j in range(maxvalue+1):
        result.append(0)
    for k in range(len(data)):
        result[data[k]] += 1
    for l in range(maxvalue+1):
        if result[l] != 0:
            for i in range(1, result[l]+1):
                results.append(l)
    if minvalue < 0:
        results = [x + minvalue for x in results]
    return results

print("\n")
print(bucket_sort(tab2))

