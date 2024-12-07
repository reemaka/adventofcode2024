import sys

f = open(sys.argv[1] if len(sys.argv) > 1 else "ex.txt", "r")
orig_lines = []
for line in f:
    orig_lines.append(line.strip())
f.close()

ans = 0
for line in orig_lines:
    test_value, nums  = line.split(':')
    test_value = int(test_value)
    nums = list(map(int, nums.strip().split(' ')))

    sums_so_far = set()
    j = 1
    while (j < len(nums)):
        if j == 1:
            add_result = nums[0] + nums[1]
            mult_result = nums[0] * nums[1]
            or_result = int(str(nums[0]) + str(nums[1]))
            sums_so_far.add(add_result)
            sums_so_far.add(mult_result)
            sums_so_far.add(or_result)
        else:
            new_sums = set()
            for sum in sums_so_far:
                add_result = sum + nums[j]
                mult_result = sum * nums[j]
                or_result = int(str(sum) + str(nums[j]))
                new_sums.add(add_result)
                new_sums.add(mult_result)
                new_sums.add(or_result)
            sums_so_far = new_sums
        j += 1
    if test_value in sums_so_far:
        ans += test_value
print(ans)