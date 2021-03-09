# -*- coding: utf-8 -*-

def FourConnectivity(i, j, mask):  
    if i < 0 or i >= row_num or j < 0 or j >= col_num or output_matrix[i][j] != 0 or input_matrix[i][j] != 1:  # cases that need to end search, such as indexing exceeds boundary 
        return 
    else:
        output_matrix[i][j] = label
        FourConnectivity(i, j - 1, mask)
        FourConnectivity(i, j + 1, mask)
        FourConnectivity(i - 1, j, mask)
        FourConnectivity(i + 1, j, mask)
        return 

input_matrix = []

with open("input_question_4", "r") as f:
    train_data = f.readlines()
    for row in train_data:
        row = row.split()
        row = list(map(int, row))
        input_matrix.append(row)
 
row_num = len(input_matrix)
col_num = len(input_matrix[0])
output_matrix = [[0 for col in range(col_num)] for row in range(row_num)] # Creat a output matrix with the same size as the input matrix   

label = 1
for i in range(row_num):
    for j in range(col_num):
        if input_matrix[i][j] == 1 and output_matrix[i][j] == 0:
            FourConnectivity(i, j, label)
            label = label + 1

with open("output_question_4", "w") as f:   
    for row in output_matrix:
        for col in range(col_num):
           f.write(str(row[col]))    
           f.write(" ")
        f.write("\n")