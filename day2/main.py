def hasla(wsad):
    valid_passwords = 0
    for line in wsad:
        policy, password = line.split(':')

        letter = policy[-1]
        min_range, max_range = map(int, policy[:-2].split('-'))

        if password.count(letter) in range(min_range, max_range + 1):
            valid_passwords += 1

    return valid_passwords


with open('input') as f:
    data = f.read()

wsad = data.splitlines()
print(hasla(wsad))