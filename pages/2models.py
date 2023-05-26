import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

rf = pickle.load(open('saved_models/rf.pkl', 'rb'))
qrf = pickle.load(open('saved_models/qrf.pkl', 'rb'))

prc = st.slider("percentage of confidence : ", 80, 100, 90, 5)

df = pd.read_csv('data/possum.csv')

df = df.drop('case', axis=1)
df = df.dropna()

df = df.reset_index(drop=True)

model_set = pd.read_csv('data/df.csv')


sexes = df['sex'].unique().tolist()
sites = df['site'].unique().tolist()

col1, col2 = st.columns(2)

with col1:
    sex = st.selectbox("choose the sex : ", sexes)
with col2:
    site = st.selectbox("choose the pop : ", sites)

df_bis = df[(df['sex'] == sex) & (df['site'] == site)].index.tolist()

try:

    ind = df_bis

    df = df.loc[ind]

    filter_set = model_set.loc[ind]

    alpha = 100 - prc

    alpha = alpha / 100

    X = filter_set.drop('age', axis=1)
    y = filter_set['age']

    preds = qrf.predict(X, [alpha/2, 0.5, 1-alpha/2])
    preds_2 = rf.predict(X)

    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.scatter(range(len(X)), y, label='True age')
    ax.scatter(range(len(X)), preds_2, label='Predicted age')
    ax.vlines(range(len(X)), preds[:, 0], preds[:, 2],
              label='Confidence interval', colors='red')
    ax.legend()

    st.pyplot(fig)

    coord = st.slider('index selection ', min_value=0,
                      max_value=len(X)-1, value=0)

    st.table(df.iloc[coord])

except:

    st.text("no data for this selection")
