def sort(nums: [int]):
    for i in range(len(nums)):

        smallestIndex = i
        for j in range(i+1, len(nums)):
            if(nums[j] < nums[smallestIndex]):
                smallestIndex = j
        temp = nums[i]
        nums[i] = nums[smallestIndex]
        nums[smallestIndex] = temp
    print(nums)
    return nums


sort([5, 6, 4, 10, 3, 15, 2, 1])
