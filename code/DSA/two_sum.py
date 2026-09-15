"""nums = [5, 9, 1, 2, 4, 15, 6, 3]
target = 13

n = len(nums)
for i in range(n-1):
    for j in range(i+1,n):

        if nums[i] + nums[j] ==target:
            print(i,j, nums[i] + nums[j])"""



"""nums = [5, 9, 1, 2, 4, 15, 6, 3]
target = 13

hash_map = {}

n = len(nums)

for i in range(n):
    colect = target - nums[i]

    if colect in hash_map:
        print([hash_map[colect],i])
        break
    hash_map[nums[i]] = i"""


