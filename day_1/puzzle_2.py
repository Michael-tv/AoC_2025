with open('puzzle_input.txt', 'r') as file:
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
print('position:', pos)
for line in content:
    print('\nInstruction:', line)
    # Determine direction
    if line[0] == 'L':
        direction = -1
    elif line[0] == 'R':
        direction = 1

    # perform rotation:
    for clicks in range(1, int(line[1:]) + 1):
        pos = (pos + direction) % 100
        # print('position:', pos)
        
        if pos == 0:
            zero_count += 1
            print('------------------')
            print('Passed Zero:', zero_count)
            print('------------------')
        

    print('Final position:', pos)

print(zero_count)