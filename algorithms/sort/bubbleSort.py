def sort(nums: [int]):
    for i in range(len(nums)):
        for j in range(0, len(nums)-1):
            if(nums[j] > nums[j+1]):
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp

    print(nums)
    return nums


sort([5, 6, 4, 10, 3, 15, 2, 1])
