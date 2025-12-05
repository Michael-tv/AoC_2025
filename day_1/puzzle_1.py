with open('day_1/puzzle_input.txt', 'r') as file:
    content = file.readlines()

# content = [
#     'L68',
#     'L30',
#     'R48',
#     'L5',
#     'R60',
#     'L55',
#     'L1',
#     'L99',
#     'R14',
#     'L82',
# ]

zero_count = 0
pos = 50
print(pos)
for line in content:
    if line[0] == 'L':
        pos = (pos - int(line[1:]))%100
    elif line[0] == 'R':
        pos = (pos + int(line[1:]))%100
    
    if pos == 0:
        zero_count += 1


    # print(pos)

print('zero count:', zero_count)


