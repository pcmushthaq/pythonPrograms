# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
def rotateLeft(d, arr):
    lastIndex = len(arr)-1
    shiftedArray = []
    for i in range(len(arr)):
        newIndex = d+i
        if newIndex > lastIndex:
            newIndex = newIndex-lastIndex-1
        shiftedArray.append(arr[newIndex])
    return shiftedArray
