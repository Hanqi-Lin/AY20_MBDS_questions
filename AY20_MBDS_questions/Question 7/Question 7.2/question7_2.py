# -*- coding: utf-8 -*-
def coor2index(coor, L):
    sum = 0
    for i in range(len(L)):
        product = 1
        for j in range(0,i):
            product = L[j] * product
        sum = sum + product * coor[i]
    return sum

def index2coor(index, L):
    coor = [0]*len(L)
    remain = index[0]
    for i in reversed(range(len(L))):
        product = 1
        for j in range(0,i):
            product = L[j] * product
        coor[i] = int(remain / product) # floor
        remain = remain - coor[i] * product
    return coor

input_coor = []
input_index = []

with open("input_coordinates_7_2.txt", "r") as f:
    next(f)
    data = f.readlines()
    for row in data:
        row = row.split()
        row = list(map(int, row))
        input_coor.append(row)

with open("input_index_7_2.txt", "r") as f:
    next(f)
    data = f.readlines()
    for row in data:
        row = row.split()
        row = list(map(int, row))
        input_index.append(row)


L = [4, 8, 5, 9, 6, 7]
output_coor = []
output_index = []
        
for coor in input_coor:
    output_index.append(coor2index(coor,L))
    
for index in input_index:
    output_coor.append(index2coor(index,L))

with open("output_index_7_2.txt", "w") as f: 
    f.write("index\n")
    for row in output_index:
        f.write(str(row))    
        f.write("\n")
        
with open("output_coordinates_7_2.txt", "w") as f:   
    f.write("x1         x2         x3         x4         x5         x6\n")
    for row in output_coor:
        for col in row:
            f.write(str(col) + "           ")  
        f.write("\n")
