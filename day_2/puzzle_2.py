with open('day_2/puzzle_input.txt', 'r') as file:
    content = file.readlines()

# content = ["""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124"""]

content = content[0].split(',')
id_ranges = []
for val in content:
    id_range = val.split('-')
    id_ranges.append((int(id_range[0]), int(id_range[1])))

def split_string_by_n(text, n):
    return [text[x:x+n] for x in range(0, len(text), n)]

# print(id_ranges)
invalid_ids = []
for id_range in id_ranges:
    for id_val in range(id_range[0], id_range[1] + 1):
        # Check for invalid ID
        str_id = str(id_val)

        # loop through all posiblilities
        # print(id_val)
        for cnt in range(1, int(len(str_id)/2) + 1):
            res = split_string_by_n(str_id, cnt)
            # print(res)
            if len(set(res)) == 1:
                invalid_ids.append(id_val)
                # print('invalid_id:', id_val)
                break

answer = sum(invalid_ids)
print(answer)      

