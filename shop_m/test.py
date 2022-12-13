


total_points = int(input())

count = 0

all_points_list = []
check = True


while check:
    if count < total_points:
        count += 1
        all_points_list.append(int(input()))
    else:
        check = False

all_points = 0

for item in all_points_list:
    all_points += item

middle_point = all_points / len(all_points_list)
need_all_points = 4*len(all_points_list)

difference = need_all_points - all_points

print(all_points_list)
print(difference)

for item in all_points_list:
    if difference >= 3:
        if item == 2:
            position = all_points_list.index(item)
            all_points_list[position] = 2 + 3
            difference -= 3
            if (all_points / len(all_points_list)) >= 4:
                print('Все')
                if difference >= 2:
                    if item == 3:
                        position = all_points_list.index(item)
                        all_points_list[position] = 3 + 1
                        difference -= 1

    elif difference < 3:
        if item == 2:
            position = all_points_list.index(item)
            all_points_list[position] = 2 + 1
            difference -= 1
        if item == 3:
            position = all_points_list.index(item)
            all_points_list[position] = 3 + 1
            difference -= 1
    else:
        pass

print(all_points_list)
print(difference)
