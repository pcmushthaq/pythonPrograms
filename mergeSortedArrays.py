def mergeSortedArrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    secondArrayIndex = 0
    firstArrayIndex = 0

    sortedArray = []
    while (secondArrayIndex < n2 and firstArrayIndex < n1):
        print('running loop')

        print(firstArrayIndex, secondArrayIndex)

        if arr1[firstArrayIndex] < arr2[secondArrayIndex]:
            sortedArray.append(arr1[firstArrayIndex])
            firstArrayIndex += 1
        else:
            sortedArray.append(arr2[secondArrayIndex])
            secondArrayIndex += 1

    while secondArrayIndex < n2:
        sortedArray.append(arr2[secondArrayIndex])
        secondArrayIndex += 1

    while firstArrayIndex < n1:
        sortedArray.append(arr1[firstArrayIndex])
        firstArrayIndex += 1

    return sortedArray


print(mergeSortedArrays([0, 2, 2, 2, 10, 20, 100], [1, 3]))
