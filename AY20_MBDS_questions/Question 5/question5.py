# -*- coding: utf-8 -*-
import copy

def color(r, b, n, R, B, L, layout, penalty):
    if r == R and b == B and n == L*L +1:
        global minimum_penalty
        global minimum_layout
        if penalty < minimum_penalty:
            minimum_penalty = penalty
            minimum_layout = copy.deepcopy(layout)

    if r < R:
        new_penalty = penalty
        if n % L != 1 and layout[n - 2] == "R":
            new_penalty += 1
        if n > L and layout[n - L - 1] == "R":
            new_penalty += 1
        layout.append("R")
        color(r + 1, b, n + 1, R, B, L, layout, new_penalty)
        layout.pop(len(layout) - 1)

    if b < B:
        new_penalty = penalty
        if n % L != 1 and layout[n - 2] == "B":
            new_penalty += 1
        if n > L and layout[n - L -1] == "B":
            new_penalty += 1
        layout.append("B")
        color(r, b + 1, n + 1, R, B, L, layout, new_penalty)
        layout.pop(len(layout) - 1)


minimum_penalty = 999999999999
minimum_layout = []

layout = []
penalty = 0
R = 12
B = 13
L = 5
color(0, 0, 1, R, B, L, layout, penalty)

output = []
print("-------layout-----\n")
for i in range(L):
    output.append(minimum_layout[i * L: (i + 1) * L])
    print(minimum_layout[i * L: (i + 1) * L])
print(minimum_penalty)


with open("output_question_5_1", "w") as f: 
    for row in output:
        for col in row:
            f.write(str(col) + " ")    
        f.write("\n")
        
