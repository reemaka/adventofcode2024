from collections import defaultdict

f = open("input.txt", "r")

l1 = []
freq = defaultdict(int)
for line in f:
  nums = line.split()
  l1.append(int(nums[0]))
  freq[int(nums[1])] += 1

score = 0
for num in l1:
  score += num * (freq[num] or 0)
print(score)
  
