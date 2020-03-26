#!/usr/bin/env python
# coding: utf-8

# # Building a Machine Learning Classifier in Python with Sci-kit Learn
# 
# Here I have implemented a simple ML algorithm called Naive Bayes(NB) classifier that predicts whether a tumor is malignant or benign.
# 
# The database used is the Breast Cancer Wisconsin Diagnostic Database
# 
# 

# In[5]:


import sklearn


# In[6]:


#import data sets

from sklearn.datasets import load_breast_cancer


# In[7]:


data=load_breast_cancer()


# In[8]:


#Loading features and targets in the form of lists

label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']


# In[9]:


#printing and having a look at our data

print(label_names)
print(labels[0])
print(feature_names[0])
print(features[0])


# In[10]:


from sklearn.model_selection import train_test_split


# In[11]:


#Getting the data ready by splitting into Train and Test splits

train, test, train_labels, test_labels = train_test_split(features,
labels,
test_size=0.33, 
random_state=42)


# *I have decided to use to Naive Bayes(NB) because the task at hand is binary classification whether the tumor is malignant or benign and NB performs well in Binary Classification*

# In[12]:


from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()


# In[13]:


model=gnb.fit(train,train_labels)


# In[14]:


# Make predictions
preds = gnb.predict(test)
print(preds)


# In[16]:


# Evaluate accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(test_labels, preds))


# This means that 94.15 percent of the time the classifier is able to make the correct prediction as to whether or not the tumor is malignant or benign

# In[ ]:




