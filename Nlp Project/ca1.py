import numpy as np
import pandas as pd
import pickle
import streamlit as st
from nltk.corpus import stopwords
from sklearn import metrics
stop = stopwords.words('english')
from sklearn.metrics import confusion_matrix #import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

test = pd.read_csv('drugsComTest_raw.csv') #train data
train = pd.read_csv('drugsComTrain_raw.csv')
merge = [train,test]
merged_data = pd.concat(merge,ignore_index=True)
merged_data.isnull().sum()/merged_data.shape[0]
merged_data['date'] = pd.to_datetime(merged_data['date'])
merged_data['year'] = merged_data['date'].dt.year  #create year
merged_data['month'] = merged_data['date'].dt.month 
merged_data['sentiment'] = merged_data["rating"].apply(lambda x: 1 if x > 5 else 0)
merged_data.dropna(inplace=True, axis=0)
vectorizer = TfidfVectorizer()
reviews_corpus = vectorizer.fit_transform(merged_data.review)
sentiment = merged_data['sentiment']
X_train,X_test,Y_train,Y_test = train_test_split(reviews_corpus,sentiment,test_size=0.33,random_state=42)
print('Train data shape ',X_train.shape,Y_train.shape)
print('Test data shape ',X_test.shape,Y_test.shape)
clf = MultinomialNB().fit(X_train, Y_train) #fit the training data

pred = clf.predict(X_test) #predict the sentiment for test data
score = clf.score(X_test, Y_test)
print("Accuracy: %s" % str(clf.score(X_test, Y_test))) #check accuracy
print("Confusion Matrix") 
print(confusion_matrix(pred, Y_test))

def app():
    text = st.text_input("Enter a text :")
    if text!=None:
        st.write(score)
        tx =[]
        tx.append(text)
        tx = vectorizer.transform(tx)
        pred1=clf.predict(tx)[0]
        if st.button('Submit'):
            st.write(pred1)
            if pred1 == 0:
                st.write("Negative")
            else:
                st.write("Postive")