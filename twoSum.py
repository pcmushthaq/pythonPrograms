# Find if there are two elements in the array which will
# give the target sum
# If there are none return false, If there is return the numbers
def twoSum(arr1, target):
    elements = {}
    for item in arr1:
        if target-item in elements:
            return [item, target-item]
        else:
            elements[item] = item
    return False

# This is an O(N) Solution..


target = 10
sampleArray = [1, 4, 2, 5, 5, 2]
print(twoSum(sampleArray, target))
