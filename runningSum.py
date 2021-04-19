
def runningSum(nums: [int]) -> [int]:
    runningSum = []
    # can remove this to further increase space complexity
    sumUptoThis = 0
    for num in nums:
        sumUptoThis += num
        runningSum.append(sumUptoThis)
    return runningSum


newArray = [1, 2, 3, 4, 5, 6]
print(runningSum(nums=newArray))
