class threesum:
    result = []
    def comb(self ,arr, k, p, temp):
        if k == len(temp):
            if (temp[0] + temp[1] + temp[2]) == 0:
                temp.sort()
                if temp not in self.result:
                    self.result.append(temp[:])
            return

        for i in range(p, len(arr)):
            temp.append(arr[i])
            self.comb(arr, k, i + 1, temp)
            del temp[-1]



val = [-1, 0, 1, 2, -1, -4]
t = [] * 3
service = threesum()
service.comb(val, 3, 0, t)

print(service.result)

