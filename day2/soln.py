import sys

def isDiffInRange(diff):
    diff = abs(diff)
    return diff > 0 and diff <= 3

def isSignSame(a, b):
    return (a < 0 and b < 0) or (a > 0 and b > 0)

def allSafe(diffs):
    return all(isDiffInRange(diff) and isSignSame(diffs[0], diff) for diff in diffs) 

def getDiffs(nums):
    i = 0
    diffs = []
    while i < len(nums) - 1:
        diff = nums[i+1] - nums[i]
        diffs.append(diff)
        i += 1
    return diffs

def getNumList(numStr):
    return list(map(int, l.split(' ')))


f = open(sys.argv[1] if len(sys.argv) > 1 else "input.txt", "r")
numList = []
for l in f:
    numList.append(getNumList(l))

sum = 0
for nums in numList:
    if len(nums) < 2:
        continue

    if allSafe(getDiffs(nums)):
        sum += 1
print(sum)

sum = 0
for nums in numList:
    if len(nums) < 2:
        continue

    if allSafe(getDiffs(nums)):
        sum += 1
        continue
    for i, num in enumerate(nums):
        alt = nums[:i] + nums[(i+1):]
        if allSafe(getDiffs(alt)):
            sum += 1
            break

print(sum)


# 1 2 7 8 9 -> +1 +5 +1 +1
# 9 7 6 2 1 -> -2 -1 -4 -1
# 1 3 2 4 5 -> +2 -1 +2 +1
# 8 6 4 4 1 -> -2 -2  0 -3