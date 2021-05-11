from typing import List


def sort(nums: List[int]):
    for i in range(1, len(nums)):
        # last index of the imaginary subarray
        j = i-1
        while j >= 0 and nums[j] > nums[j+1]:
            temp = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = temp
            j = j-1
            # See how many loops are run
            print(nums)

    print(nums)
    return nums


sort([5, 6, 4, 10, 3, 15, 2, 1])
print('\n\n\n\n\n')
# See how efficient it is for nearly sorted lists
sort([1, 2, 3, 4, 5, 7, 6, 8])
