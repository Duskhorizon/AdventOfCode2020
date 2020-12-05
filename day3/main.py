from functools import reduce 

def trees_check(data, right, down):
    index = 0
    trees = 0
    for i in range(0, len(data), down):
        if data[i][index] == '#':
            trees+=1
        index = (index+right)%len(data[0])
    return trees

with open("input", 'r') as file:
    data = file.read().splitlines()
    print('czesc 1 {}'.format(trees_check(data, 3, 1)))
    print('czesc 2: {}'.format(reduce((lambda x,y:x*y), [trees_check(data, right, down) for right, down in [(1,1),(3,1),(5,1),(7,1),(1,2)]])))