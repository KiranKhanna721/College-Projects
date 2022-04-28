import numpy as np
import pandas as pd
import pickle
import streamlit as st
from nltk.corpus import stopwords
from sklearn import metrics
stop = stopwords.words('english')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split
df = pd.read_csv('drugsComTrain_raw.csv', sep=',')
df_train = df[(df['condition']=='Birth Control') | (df['condition']=='Depression') | (df['condition']=='High Blood Pressure')|(df['condition']=='Diabetes, Type 2')| (df['condition']=='Pain')|(df['condition']=='Insomnia')|(df['condition']=='Anxiety')|(df['condition']=='Weight Loss')|(df['condition']=='Obesity')|(df['condition']=='ADHD')|(df['condition']=='Chronic Pain')|(df['condition']=='Bipolar Disorde')|(df['condition']=='Emergency Contraception')|(df['condition']=='Acne')|(df['condition']=='Vaginal Yeast Infection')]
X = df_train.drop(['uniqueID','drugName','rating','date','usefulCount'],axis=1)
for i, col in enumerate(X.columns):
    X.iloc[:, i] = X.iloc[:, i].str.replace('"', '')
X_feat=X['review']
y=X['condition']
X_train, X_test, y_train, y_test = train_test_split(X_feat, y,test_size=0.2, random_state=0)
tfidf_vectorizer3 = TfidfVectorizer(stop_words='english', max_df=0.8, ngram_range=(1,3))
tfidf_train_3 = tfidf_vectorizer3.fit_transform(X_train)
tfidf_test_3 = tfidf_vectorizer3.transform(X_test)
pass_tf2 = PassiveAggressiveClassifier()
pass_tf2.fit(tfidf_train_3, y_train)
pred = pass_tf2.predict(tfidf_test_3)
score = metrics.accuracy_score(y_test, pred)
def app():
    text = st.text_input("Enter a text :")

    if text!=None:
        st.write(score)
        tx =[]
        tx.append(text)
        tx = tfidf_vectorizer3.transform(tx)
        pred1=pass_tf2.predict(tx)[0]
        if st.button('Submit'):
            st.write(pred1)