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

def hamming(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

for idx, val in enumerate(content):
    for val2 in content[idx+1:]:
        if hamming(val, val2) == 1:
            print val
            print val2
