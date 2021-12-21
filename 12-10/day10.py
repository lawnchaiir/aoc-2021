
with open("input.txt", "r") as f:
    lines = f.readlines()

scope_chars = {
    "{" : "}",
    "(" : ")",
    "<" : ">",
    "[" : "]"
}

score_values_pt_1 = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

score_values_pt_2 = {
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4
}

def parse_line_pt_1(line, stack):
    for c in line:
        if c in scope_chars: # it's an open char
            stack.append(c)
        else:
            curr_scope = stack.pop()
            close_char = scope_chars[curr_scope]
            if c != close_char:
                score = score_values_pt_1[c]
                return score
    return 0

def parse_line_pt_2(line, stack):
    for c in line:
        if c in scope_chars: # it's an open char
            stack.append(c)
        else:
            curr_scope = stack.pop()
            close_char = scope_chars[curr_scope]
            if c != close_char:
                return 0
    score = 0

    while stack:
        open_scope = stack.pop()
        close_char = scope_chars[open_scope]
        char_score = score_values_pt_2[close_char]
        score *= 5
        score += char_score

    return score

stack = []
total_score = 0
for line in lines:
    stack.clear()
    line = line.strip()
    score = parse_line_pt_1(line, stack)
    total_score += score

print("pt 1 score", total_score)

all_scores = []
for line in lines:
    stack.clear()
    line = line.strip()
    score = parse_line_pt_2(line, stack)

    if score != 0:
        all_scores.append(score)

all_scores.sort()

def ceildiv(a, b):
    return -(-a // b)

mid_point = ceildiv(len(all_scores) -1, 2)

print(all_scores[mid_point])

