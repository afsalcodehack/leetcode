def combination(arr, start, result, r):
    if start == r:
        print(result)
        return
    for i in range(start, len(arr)-1):
        result[start] = arr[i]
        combination(arr, start + 1, result, r)

data = [0] * 3
combination([1, 2, 3, 4], 0, data, 3)
