def comb(arr, l, p, temp):

    if l == len(temp):
        print(temp)
        return

    for i in range(p, len(arr)):
        temp.append(arr[i])
        comb(arr, l, i + 1, temp)
        del temp[-1]

val = [-1, 0, 1, 2,-1,-4]
t = [] * 3
comb(val, 3, 0, t)
