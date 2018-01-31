with open('temp1', 'r') as f:
    content = f.readlines()

content = [x.strip() for x in content] 
nums = [int(x) for x in content]
print sum(nums)