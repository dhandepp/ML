# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:39:49 2019

@author: mayur
"""
from sklearn import tree
features = [[140,1],[130,1],[150,0],[170,0]]
labels = ["apple","apple","orange","orange"]
model = tree.DecisionTreeClassifier()
model = model.fit(features,labels)
print(model.predict([[150,0]]))

