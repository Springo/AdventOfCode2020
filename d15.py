inp = "13,0,10,12,1,5,8".split(',')
nums = [int(n) for n in inp]

spoken = dict()
for i in range(len(nums) - 1):
    spoken[nums[i]] = i + 1

turns = len(nums)
last = nums[-1]

#while turns < 2020:
while turns < 30000000:
    turns += 1
    if last in spoken:
        newnum = turns - spoken[last] - 1
        spoken[last] = turns - 1
        last = newnum
    else:
        spoken[last] = turns - 1
        last = 0

print(last)
