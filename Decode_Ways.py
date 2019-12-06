def decode_ways(nums, result, start, end):
    if len(nums) == end:
        print(result)
        return

    result.append(nums[start:end + 1])

    decode_ways(nums, result, start + 1, start + 1)

    result = result[:-1]

    if end <= len(nums)-2:
        decode_ways(nums, result, start + 1, start + 2)


res = []
decode_ways("1234", res, 0, 0)
