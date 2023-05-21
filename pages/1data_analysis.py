import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dython.nominal import associations

df = pd.read_csv("data/possum.csv")
df = df.drop('case', axis=1)

numerical_col = ['hdlngth', 'skullw', 'totlngth', 'taill',
                 'footlgth', 'earconch', 'eye', 'chest', 'belly', 'age']
col_to_encod = ['site', 'Pop', 'sex']

# Titre centré avec emoji
st.title('📊 Data Analysis')

# Introduction centrée
st.markdown(
    """
    The Possum dataset contains information about 104 possums. The recorded variables include morphological measurements such as head and body length, tail length, limb length, and other specific features of each possum. 🐾
    """
)

# Ajout d'espaces
st.write("\n\n")

# Sous-titre centré
st.subheader('📝 Overview of the first data')

# Tableau centré
st.table(df.head())

# Ajout d'espaces
st.write("\n\n")

# Sous-titre centré
st.subheader('📊 Boxplots and distribution of numerical variables')

# Création des figures pour les boxplots
fig, axs = plt.subplots(ncols=2, nrows=5, figsize=(7, 12))
index = 0
axs = axs.flatten()
for k, v in df[numerical_col].items():
    sns.boxplot(y=k, data=df[numerical_col], ax=axs[index])
    index += 1
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)

# Affichage de la figure centrée
st.pyplot(fig)

# Ajout d'espaces
st.write("\n\n")

# Création des figures pour les distributions
fig, axs = plt.subplots(ncols=2, nrows=5, figsize=(7, 12))
index = 0
axs = axs.flatten()
for k, v in df[numerical_col].items():
    sns.distplot(v, ax=axs[index], kde_kws={'bw_method': 0.1})
    index += 1
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)

# Affichage de la figure centrée
st.pyplot(fig)

# Ajout d'espaces
st.write("\n\n")

# Sous-titre centré
st.subheader(
    '📊 Correlation between all variables using the dython package')

# Calcul et affichage de la corrélation
corr = associations(df, nominal_columns=col_to_encod,
                    compute_only=True)['corr']
fig2, ax2 = plt.subplots(figsize=(20, 20))
ax2 = sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
                  vmin=-1, vmax=1, center=0, linewidths=3, linecolor='black', cbar=False, annot_kws={"fontsize": 25})
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45,
                    horizontalalignment='right', fontsize=25)
ax2.set_yticklabels(ax2.get_yticklabels(), rotation=45,
                    horizontalalignment='right', fontsize=25)
# Affichage de la figure centrée
st.pyplot(fig2)
