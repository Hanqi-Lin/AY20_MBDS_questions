# -*- coding: utf-8 -*-
def coor2index(coor, L):
    index = coor[1] * L[0] + coor[0]
    return index

def index2coor(index, L):
    coor = []
    coor.append(int(index[0] % L[0]))
    coor.append(int(index[0] / L[0])) # floor
    return coor

input_coor = []
input_index = []

with open("input_coordinates_7_1.txt", "r") as f:
    next(f)
    data = f.readlines()
    for row in data:
        row = row.split()
        row = list(map(int, row))
        input_coor.append(row)

with open("input_index_7_1.txt", "r") as f:
    next(f)
    data = f.readlines()
    for row in data:
        row = row.split()
        row = list(map(int, row))
        input_index.append(row)


L = [50, 57]
output_coor = []
output_index = []
        
for coor in input_coor:
    output_index.append(coor2index(coor,L))
    
for index in input_index:
    output_coor.append(index2coor(index,L))

with open("output_index_7_1.txt", "w") as f: 
    f.write("index\n")
    for row in output_index:
       f.write(str(row))    
       f.write("\n")
        
with open("output_coordinates_7_1.txt", "w") as f:   
    f.write("x1    x2\n")
    for row in output_coor:
       f.write(str(row[0]) + "    " + str(row[1]))    
       f.write("\n")
    