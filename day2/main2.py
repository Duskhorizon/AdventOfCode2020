def hasla(wsad):
    valid = 0
    for line in wsad:
        policy, password = line.split(':')

        letter = policy[-1]
        index1, index2 = map(int, policy[:-2].split('-'))
        pos1, pos2 = password[index1] == letter, password[index2] == letter
        
        if (pos1 and not pos2) or (not pos1 and pos2):
            valid += 1

    return valid


with open('input') as f:
    data = f.read()

wsad = data.splitlines()
print(hasla(wsad))