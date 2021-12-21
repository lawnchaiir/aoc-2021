
with open("input.txt", "r") as f:
    lines = f.readlines()

scope_chars = {
    "{" : "}",
    "(" : ")",
    "<" : ">",
    "[" : "]"
}

score_values = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

def parse_line(line, stack):
    for c in line:
        if c in scope_chars: # it's an open char
            stack.append(c)
        else:
            curr_scope = stack.pop()
            close_char = scope_chars[curr_scope]
            if c != close_char:
                score = score_values[c]
                return score
    return 0

stack = []
total_score = 0
for line in lines:
    stack.clear()
    line = line.strip()
    score = parse_line(line, stack)
    total_score += score

print(total_score)