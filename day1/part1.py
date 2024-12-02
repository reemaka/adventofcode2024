f = open("ex.txt", "r")

l1 = []
l2 = []
for line in f:
  nums = line.split()
  l1.append(int(nums[0]))
  l2.append(int(nums[1]))

l1.sort()
l2.sort()

i = 0
sum = 0
while i < len(l1):
  sum += abs(l1[i] - l2[i])
  i += 1
print(sum)
