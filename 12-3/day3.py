

with open("input.txt", "r") as f:
    lines = f.readlines()

line_length = len(lines[0]) - 1

one_counts = [0 for x in range(line_length)]
zero_counts = [0 for x in range(line_length)]

for line in lines:
    for idx, c in enumerate(line):
        if c == '1':
            one_counts[idx] += 1
        elif c == '0':
            zero_counts[idx] += 1

print(one_counts)
print(zero_counts)

gamma = ""
epsilon = ""

for i in range(line_length):
    if one_counts[i] > zero_counts[i]:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(gamma)
print(epsilon)

gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)

print(gamma_int, epsilon_int)
print(gamma_int * epsilon_int)

lines.sort()

def find_prefix_range(lst, prefix, low = None, high = None):
    low = low or 0
    high = high or len(lst) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if lst[mid].startswith(prefix):
            high = mid - 1
        elif lst[mid] < prefix:
            low = mid + 1
        else:
            high = mid

    lower_bound = low

    seq_len = 0
    for i in range(lower_bound, len(lst)):
        if lst[i].startswith(prefix):
            seq_len += 1
        else:
            break

    return lower_bound, seq_len


def get_o2_search_string(start_string, range_start, range_end, selector):
    s = start_string
    pos = len(s)
    zeroes = 0
    ones = 0
    for i in range(range_start, range_end):
        line = lines[i]
        if line[pos] == "1":
            ones +=1
        elif line[pos] == "0":
            zeroes += 1
    
    if selector(zeroes, ones):
        s += "0"
    else:
        s += "1"
    
    return s

o2_candidates = 0
o2_search = ""

search_start = 0
search_end = len(lines)

while o2_candidates != 1:
    o2_search = get_o2_search_string(o2_search, search_start, search_end, lambda z, o: o < z)
    start, count = find_prefix_range(lines, o2_search)
    if count == 0:
        break
    search_start = start
    search_end = start + count
    o2_candidates = count

o2_rating = int(lines[search_start], 2)
print(o2_rating)

co2_candidates = 0
co2_search = ""

search_start = 0
search_end = len(lines)

while co2_candidates != 1:
    co2_search = get_o2_search_string(co2_search, search_start, search_end, lambda z, o: z <= o)
    start, count = find_prefix_range(lines, co2_search)
    if count == 0:
        break
    search_start = start
    search_end = start + count
    co2_candidates = count

co2_rating = int(lines[search_start], 2)
print(co2_rating)

print(o2_rating * co2_rating)
