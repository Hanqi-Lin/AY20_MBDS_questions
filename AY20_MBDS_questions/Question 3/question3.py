# -*- coding: utf-8 -*-
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import numpy as np

feature=[]
target=[]
test=[]

with open("train_data.txt", "r") as f:
    next(f)
    train_data = f.readlines()
    for line in train_data:
        numbers = line.split()
        numbers_float = list(map(float, numbers))
        feature.append(numbers_float)

with open("train_truth.txt", "r") as f:
    next(f)
    train_truth = f.readlines()
    for line in train_truth:
        numbers = line.split()
        numbers_float = list(map(float, numbers))
        target.append(numbers_float)

with open("test_data.txt", "r") as f:
    next(f)
    test_data = f.readlines()
    for line in test_data:
        numbers = line.split()
        numbers_float = list(map(float, numbers))
        test.append(numbers_float)
        
feature = np.array(feature)
target = np.array(target)
test = np.array(test)

feature.reshape(1, -1)
target = target.ravel()

feature_train, feature_test, target_train, target_test = train_test_split(feature, target, test_size=0.2,random_state=0)

clf = MLPRegressor(solver='adam',hidden_layer_sizes=(4,4),random_state=2)


clf.fit(feature_train,target_train)
print("clf.score is %0.2f" % clf.score(feature_test, target_test))
scores = cross_val_score(clf, feature, target)
print("%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std()))

predict_results=clf.predict(test)

with open("test_predicted.txt", "w") as f:  
    f.write("y" + "\n") 
    for line in predict_results:    
           f.write(str(line))    
           f.write("\n")

