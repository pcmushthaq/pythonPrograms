# Given an array of integers nums.

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.

def numIdenticalPairs(self, nums: [int]) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] == nums[j]):
                count += 1

    return count
