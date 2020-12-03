with open("input") as wsad:
    data = wsad.read().splitlines()

for i in range(len(data)-1):
    for z in range(len(data)):
        if int(data[i]) + int(data[z]) == 2020:
            print(int(data[i]) * int(data[z]))