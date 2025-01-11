import re

f = open("./day-3.txt", "r")
x = f.read()

lines = x.split("\n")[:-1]

all_matches = [list(re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", line)) for line in lines]

pairs = [
    [int(match.group(1)), int(match.group(2))]
    for matches_in_line in all_matches
    for match in matches_in_line
]

multiplications = [x[0] * x[1] for x in pairs]

print(sum(multiplications))

# --- 2nd star solution

all_matches = [
    list(re.finditer(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)", line))
    for line in lines
]

enabled = True
pairs = []

for matches_in_line in all_matches:
    for match in matches_in_line:
        if match.group(0) == "do()":
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
        else:
            if enabled:
                pairs.append([int(match.group(1)), int(match.group(2))])

multiplications = [x[0] * x[1] for x in pairs]

print(sum(multiplications))
