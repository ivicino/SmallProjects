# Decision Tree Algorithm
# from https://www.simplilearn.com/tutorials/machine-learning-tutorial/decision-tree-in-python
# and https://www.datacamp.com/tutorial/decision-tree-classification-python

import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn import metrics

col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
# load dataset
pima = pd.read_csv(".\Documents\PythonCode\Pima Indians Diabetes Database\diabetes.csv", header=None, names=col_names)
# print(pima.head(20))

# # It is interesting that the tutorial didn't one-hot encode the data. I'm gonna do that now
# pima = pd.get_dummies(pima)
# print(pima)
# # I think it's because this data does not need to be one-hot encoded...

"""Preprocessing the data"""
#split dataset in features and target variable
feature_cols = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
X = pima[feature_cols] # Features
y = pima.label # Target variable
# print(pima.pregnant) # Oh thats how that works... Cool! I didn't know that!


# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 



"""Decision Tree"""
# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer/ make decision tree (requires the features and the label values)
clf = clf.fit(X_train,y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# We got a classification rate of 0.6883116883116883 or 68%, which is apparently considered as good accuracy. 
# I thought that was terrible but I'm used to neural networks...

# """Visualizing the unprunned Decision Tree"""
# import matplotlib.pyplot as plt
# from sklearn import tree

# fig = plt.figure(figsize=(10,10))
# _ = tree.plot_tree(clf, 
#                    feature_names=feature_cols,  
#                    class_names='hasDiabetes',
#                    filled=True)
# plt.show()


"""PRUNNING the Tree"""

"""Decision Tree"""
# Create Decision Tree classifer object
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)

# Train Decision Tree Classifer/ make decision tree (requires the features and the label values)
clf = clf.fit(X_train,y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# We got a classification rate of 0.6883116883116883 or 68%, which is apparently considered as good accuracy. 
# I thought that was terrible but I'm used to neural networks...

"""Visualizing the unprunned Decision Tree"""
import matplotlib.pyplot as plt
from sklearn import tree

fig = plt.figure(figsize=(10,7))
_ = tree.plot_tree(clf, 
                   feature_names=feature_cols,  
                   class_names='01',
                   filled=True)
plt.show()

# The prunned tree has a way better accuracy! by both making the criterion = 'entropy' and limiting the depth to 3