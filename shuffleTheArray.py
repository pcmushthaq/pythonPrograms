def shuffle(self, nums: [int], n: int) -> [int]:
    newArray=[]
    for i in range(n):
        newArray.append(nums[i])
        newArray.append(nums[n+i])
    return newArray

#[1,2,3,4,5,6]=>[1,4,2,5,4,6] where n=3