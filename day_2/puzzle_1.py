with open('day_2/puzzle_input.txt', 'r') as file:
    content = file.readlines()

content = content[0].split(',')
id_ranges = []
for val in content:
    id_range = val.split('-')
    id_ranges.append((int(id_range[0]), int(id_range[1])))

# print(id_ranges)
invalid_ids = []
for id_range in id_ranges:
    for id_val in range(id_range[0], id_range[1] + 1):
        # Check for invalid ID
        str_id = str(id_val)
        if str_id[:int(len(str_id)/2)] == str_id[int(len(str_id)/2):]:
            invalid_ids.append(id_val)

answer = sum(invalid_ids)
print(answer)      

