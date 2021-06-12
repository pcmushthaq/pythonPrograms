def hourglassSum(arr):
    sums = []
    for i in range(1, 5):
        for p in range(1, 5):
            total = arr[i][p]
            for j in range(-1, 2, 2):
                for k in range(-1, 2):
                    #print(j, k)
                    # print(arr[i-j][p-k])
                    total += arr[i-j][p-k]

            print(total)
            sums.append(total)

    return max(sums)


arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [
    1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0], ]
# for _ in range(6):
#     arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)
print(result)
