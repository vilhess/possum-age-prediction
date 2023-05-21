import streamlit as st

# Titre de la page
st.markdown("<h1 style='font-size: 36px;'>🐾 Prédiction de l'âge des possums 📊</h1>",
            unsafe_allow_html=True)

st.subheader("")
st.subheader("")
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style='text-align: center;'>
            <p style='font-size: 25px;'>🐾 The Possum Dataset contains information about 100 possums, including morphological measurements such as head length, body length, tail length, and limb length.</p>
            <p style='font-size: 25px;'>Our goal is to analyze the dataset, explore the variables, and establish correlations between them. 🔍 We will use methods like boxplots and regression modeling to understand the relationships between the variables and possum age. 📈</p>
            <p style='font-size: 25px;'>This research aims to enhance our knowledge of possum development and contribute to conservation and ecological studies. 🌱</p>
            <p style='font-size: 25px;'>Please note that the results are specific to the Possum Dataset. 📊</p>
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    st.subheader('')
    st.subheader('')
    st.subheader('')
    st.subheader('')
    st.subheader('')
    st.subheader('')
    st.image('pic/possum.jpg', use_column_width=True)
