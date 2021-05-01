# Given the array nums,
# for each nums[i] find out how many numbers
#  in the array are smaller than it. That is,
# \for each nums[i] you have to count the number
#  of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

# O(n) solution
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         count = [0] * 102
#         for num in nums:
#             count[num+1] += 1
#         for i in range(1, 102):
#             count[i] += count[i-1]
#         return [count[num] for num in nums]

def bruteForce(nums: [int]):
    resultArray = list(map(lambda x: 0, nums))
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if(nums[i] > nums[j]):
                resultArray[i] += 1

    print(resultArray)


def smallerNumbersThanCurrent(nums: [int]):
    indices = {}
    resultArray = enumerate(sorted(nums))
    for index, num in resultArray:
        print(index, num)
        indices.setdefault(num, index)
    print([indices[num] for num in nums])


bruteForce([8, 4, 2, 1, 2, 3])
smallerNumbersThanCurrent([8, 4, 2, 1, 2, 3])
