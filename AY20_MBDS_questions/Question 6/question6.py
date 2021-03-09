# -*- coding: utf-8 -*-
def RayCasting(point, line_o, line_e):
    if line_o[1] == line_e[1]: # cases that are parallel or overlap
        return False
    if point[1] == line_o[1] and point[1] < line_e[1]: # intersect with origin
        return False
    if point[1] > line_o[1] and point[1] == line_e[1]: # intersect with end
        return False
    if line_o[1] > point[1] and line_e[1] > point[1]: # line above point
        return False
    if line_o[1] < point[1] and line_e[1] < point[1]: # line beneath point
        return False
    if point[0] > line_o[0] and point[0] > line_e[0]: # line locates on the left of point 
        return False
    
    intersect = line_e[0]-(line_e[0]-line_o[0])*(line_e[1]-point[1])/(line_e[1]-line_o[1])
    if intersect < point[0]:
        return False
    else:
        return True

def isPointInside(point,poly):
    intersect_count = 0
    i = 0
    while i < len(poly):
        if RayCasting(point,poly[i-1],poly[i]):
            intersect_count = intersect_count + 1
        i = i + 1
    if (intersect_count % 2) == 1:
        return True
    else:
        return False

points = []
poly = []
results = []

with open("input_question_6_points", "r") as f:
    data = f.readlines()
    for line in data:
        point = line.split()
        point_int = list(map(int, point))
        if point_int != []:
            points.append(point_int)


with open("input_question_6_polygon", "r") as f:
    data = f.readlines()
    for line in data:
        point = line.split()
        point_int = list(map(int, point))
        poly.append(point_int)
    
for point in points:
    if isPointInside(point,poly):
        results.append([point[0],point[1],'inside'])
    else:
        results.append([point[0],point[1],'outside'])
        
        
with open("output_question_6", "w") as f:   
    for line in results:   
           f.write(str(line[0]) + " " + str(line[1]) + " " + str(line[2]))    
           f.write("\n")
    
    