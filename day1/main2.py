with open("input") as wsad:
    data = wsad.read().splitlines()

for i in range(len(data)):
    for z in range(len(data)):
        for y in range(len(data)):
            if int(data[i]) + int(data[z]) +int(data[y]) == 2020:
                print(int(data[i]) * int(data[z]) * int(data[y]))