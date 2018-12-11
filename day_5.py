import string

with open('day_5_input.txt', 'r') as f:
    data = f.read()


def cmp_letters(a, b):
    return a.upper() == b.upper() and a!=b


def react(chain):
    keep_going = True
    while keep_going:
        keep_going = False
        for idx in range(len(chain)-1):
            if cmp_letters(chain[idx], chain[idx+1]):
                chain = chain[:idx] + chain[idx+2:]
                keep_going = True
                break
    return len(chain)

letters = list(string.ascii_lowercase)
for l in letters:
    print "{}: ".format(l), react(data.replace(l, "").replace(l.upper(), ""))
