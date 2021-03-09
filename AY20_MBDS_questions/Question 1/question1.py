# -*- coding: utf-8 -*-
def find_operations(operations, desired_sum, sum, m, n, m_max, n_max):
    global flag
    if flag == 1: # comment flag if only one solution is required
        return
    if desired_sum - (1 + m_max) * m_max / 2 - m_max * (n_max) > 0 or desired_sum - (1 + m_max) * m_max / 2 - n_max < 0:
        print(str(desired_sum) + " no solution")
        output.append([str(desired_sum) + " no solution"])
        return 
    if sum - (m + 1 + m_max) * (m_max - m) / 2 - m_max * (n_max - n) > 0 or sum - (m + 1 + m_max) * (m_max - m) / 2 - m * (n_max - n) < 0:
        return
    if m == m_max and n == n_max and sum == 0:
        print(str(desired_sum),operations)
        output.append([str(desired_sum) + " " + operations])
        flag = 1
        return
    if m < m_max and sum - m -1 >= 0:
        find_operations(operations + "D", desired_sum, sum - m -1, m + 1, n, m_max, n_max)
    if n < n_max and sum - m >= 0:
        find_operations(operations + "R", desired_sum, sum - m, m, n + 1, m_max, n_max)
    return


desired_sum = [65,75,90,110]
m = 9
n = 9
output = []

for i in desired_sum:
    flag = 0
    operations = ""
    find_operations(operations,i, i - 1, 1, 1, m, n)

    
desired_sum = [87127231192]
m = 90000
n = 100000

for i in desired_sum:
    flag = 0
    operations = ""
    find_operations(operations,i, i - 1, 1, 1, m, n)
    

with open("output_question_1", "w") as f:
    for row in output:
        f.write(str(row[0]))    
        f.write("\n")