from typing import List


def mergeSort(nums: List):
    if(len(nums) == 1):
        return nums
    middle = len(nums)//2
    left = nums[0:middle]
    right = nums[middle:]

    return merge(mergeSort(left), mergeSort(right))


def merge(left: List, right: List):
    j = 0
    i = 0
    newList = []
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            newList.append(left[i])
            i += 1
        else:
            newList.append(right[j])
            j += 1
    while (i < len(left)):
        newList.append(left[i])
        i += 1
    while (j < len(right)):
        newList.append(right[j])
        j += 1
    print('Divided List', newList)
    return newList


sample = [958, 5, 2, 8, 3, 0, 1, 9, 2, 7, 45, 123, 6, 11, 67]
print(mergeSort(sample))
