boarding_passes = open('input').read().splitlines()

def calculate_coord(seat_data,minv,maxv):
    dec = maxv/2
    for letter in seat_data:
        if letter == "F" or letter == "L":
            maxv = maxv-dec
            dec = dec/2
        if letter ==  "B" or letter == "R":
            minv = minv+dec
            dec = dec/2
    return maxv

def get_seat_id(bpass):
    row = calculate_coord(bpass[0:7],1,128) - 1
    column = calculate_coord(bpass[-3:],1,8) - 1
    seat_id = row * 8 + column
    return int(seat_id)

def find_my_seat(seat_list):
    for i in range(int(max(map(get_seat_id,boarding_passes)))):
        if i not in seat_list:
            if i+1 in seat_list and i-1 in seat_list:
                return i

print ('1st part:',max(map(get_seat_id,boarding_passes)))
print('2nd part:',find_my_seat(list(map(get_seat_id,boarding_passes))))


