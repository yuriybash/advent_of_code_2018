with open('day_3_input', 'r') as f:
    content = [x.strip() for x in f.readlines()]

for l in content:
    id_ = l[1:l.index(" ")]
    left_outer = int(l[l.index('@')+2:l.index(',')])
    vertical_outer = int(l[l.index(',')+1:l.index(':')])
    width = int(l[l.index(':')+2:l.index('x')])
    height = int(l[l.index('x')+1:])

    for row_idx in xrange(vertical_outer, vertical_outer+height):
        for col_idx in xrange(left_outer, left_outer+width):
            if grid[row_idx][col_idx] == 0:
                grid[row_idx][col_idx] = id_
            else:
                grid[row_idx][col_idx] = 'X'


flat_list = [item for sublist in grid for item in sublist]

for l in content:
    id_ = l[1:l.index(" ")]
    width = int(l[l.index(':')+2:l.index('x')])
    height = int(l[l.index('x')+1:])

    expected_count = width*height
    actual_count = flat_list.count(id_)
    if expected_count == actual_count:
        print "solution: ", id_
        break
