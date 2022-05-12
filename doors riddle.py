doors = {}

for i in range(1,101):
    doors[i] = 'c'

for person in range(1,101):
    for door in range(0+person,101, person):
        if doors[door] == 'c':
            doors[door] = 'o'
        elif doors[door] == 'o':
            doors[door] = 'c'

pairs = doors.items()
opened = {key: value for key, value in pairs if value == 'o'}

print(opened)