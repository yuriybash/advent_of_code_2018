temp_sum = 0
prev_sums = set()
while True:
    for x in nums:
        temp_sum += x
        if temp_sum in prev_sums:
            print "solution to part 1: ", temp_sum
            break
        else:
            prev_sums.add(temp_sum)


twos = 0
threes = 0

for l in content:
    count = defaultdict(lambda: 0)
    for c in l:
        count[c] += 1
    if 2 in count.values():
        twos+=1
    if 3 in count.values():
        threes+=1
print "solution to part 2: ", twos*threes
