# Given an array of integers, find the first
# recurring element
# Eg;[1,0,4,5,1,2] returns 1


def findFirstRecurringElement(array):
    elementMap = dict()
    for element in array:
        if element in elementMap:
            return element
        else:
            elementMap[element] = True


testArray = [1, 4, 5, 3, 15, 25, 13, 46, 14, 1]
element = findFirstRecurringElement(testArray)
print(element)
