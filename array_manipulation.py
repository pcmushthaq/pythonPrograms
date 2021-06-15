# Starting with a 1-indexed array of zeros and a list of
# operations, for each operation add a value to each the
# array element between two given indices, inclusive.
# Once all operations have been performed, return the
# maximum value in the array.

# https://www.hackerrank.com/challenges/crush/problem

def arrayManipulation(n, queries):
    # Brute Force Solution, Ineffective for large values

    # array=[0]*n
    # for query in queries:
    #     startIndex=query[0]
    #     endIndex=query[1]
    #     value=query[2]
    #     for i in range(startIndex-1,endIndex):
    #         array[i]+=value
    # return max(array)

    # Here we will just add the slopes at the beginning index
    # and endIndex. In the end find the maximum of cumulative sum
    array = [0]*n
    for query in queries:
        startIndex = query[0]-1
        endIndex = query[1]
        value = query[2]
        array[startIndex] += value
        if(endIndex < n):
            array[endIndex] -= value
    prevSum = 0
    maxValue = 0
    for num in array:
        prevSum += num
        maxValue = max(maxValue, prevSum)
    return maxValue
