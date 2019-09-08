def comb(arr, l, p, temp):
    if l == len(temp):
        print(temp)
        return

    for i in range(p, len(arr)):
        temp.append(arr[i])
        comb(arr, l, p+1, temp)
        del temp[-1]

arr = [-1, 0, 1, 2, -1, -4];
temp = []*3
comb(arr,3,0,temp)