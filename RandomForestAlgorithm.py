# Random Forest Algorithm
# based on https://www.datacamp.com/tutorial/random-forests-classifier-python


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
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



"""unprunned Random Forest"""
rf = RandomForestClassifier(max_depth=4)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
# The random forest algorithm seems to be more accurate than the decision tree algorithm...
# changing the criterion doesn't really help...
# but modifying the max_depth does!






"""Visualizing three examples of Decision Trees in the Random Forest"""
import matplotlib.pyplot as plt
from sklearn import tree

# for i in range(3):
#     tree1 = rf.estimators_[i]
#     fig = plt.figure(figsize=(5,5))
#     _ = tree.plot_tree(tree1, 
#                     feature_names=feature_cols,  
#                     class_names='01',
#                     filled=True)
# plt.show()

# print(rf.estimator_)


"""Figuring out which Feature had the most importance toward determing if patient would get Diabetes"""
# Create a series containing feature importances from the model and feature names from the training data
feature_importances = pd.Series(rf.feature_importances_, index=X_train.columns).sort_values(ascending=False)

# Plot a simple bar chart
feature_importances.plot.bar()

plt.show()

