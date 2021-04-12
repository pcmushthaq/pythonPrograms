# # check if two arrays contains common items

def contain_common_item(arr1, arr2):
    map = {}
    for item in arr1:
        if(item not in map):
            map[item] = True

    for item in arr2:
        if(item in map):
            return item

    return False


arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 1, 9]
print('Contains Common Item?')
print(contain_common_item(arr1, arr2))
