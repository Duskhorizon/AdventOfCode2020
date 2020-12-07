def find_missing(numbers):
    numbers = sorted(numbers)
    return [x for x in range(numbers[0], numbers[-1]+1) if x not in numbers]

boarding = open('input').read().strip().split('\n')

freplace = lambda s, d: s if not d else freplace(s.replace(*d.pop()), d)
highest = 0
seats = []

for passes in boarding:
    replaces = [('F','0'), ('B','1'), ('L','0'), ('R','1')]
    bpass = freplace(passes, replaces)
    seat = int(bpass[:7], 2) * 8 + int(bpass[-3:], 2)
    seats.append(seat)
    highest = max(highest, seat)

print(highest) #part1
print(find_missing(seats)[0]) #part2