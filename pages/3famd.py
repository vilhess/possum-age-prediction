import streamlit as st
from prince import FAMD
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder

st.title('Factor Analysis of Mixed Data (FAMD)')


@st.cache_resource(experimental_allow_widgets=True)
def func():

    full = pd.read_csv('data/possum.csv')
    full = full.drop('case', axis=1)
    full = full.dropna()

    n_comp = 14

    famd = FAMD(n_components=n_comp, n_iter=10, random_state=100)

    famd.fit(full)

    summary = famd.eigenvalues_summary['% of variance (cumulative)']

    return famd, summary, full


famd, summary, full = func()


def p_var():

    st.pyplot(pd.DataFrame(
        famd.cumulative_percentage_of_variance_).plot.bar().figure)


# p_var()


def col_contrib():
    comp_cons = st.slider("Number of components : ", 1, 14, 1, 1)

    st.pyplot(famd.column_contributions_[
        comp_cons-1].sort_values(ascending=False).plot.bar(figsize=(20, 10)).figure)

    st.subheader(f"We conserve {summary[comp_cons - 1]} of the variance")

    st.subheader('')
    st.subheader('')
    st.subheader(
        'Graph of the ACP')

    filter = st.selectbox("Choose the filter", ['sex', 'site'])

    try:

        le = LabelEncoder()
        aa = le.fit_transform(full[filter])
        mapping = dict(zip(le.classes_, range(len(le.classes_))))
        scatter_x = famd.row_coordinates(full)[comp_cons-1]
        scatter_y = famd.row_coordinates(full)[comp_cons]
        group = aa
        cdict = mapping

        fig = plt.figure(figsize=(15, 10))
        ax = fig.add_subplot(1, 1, 1)
        for g in np.unique(group):
            ix = np.where(group == g)
            key = [k for k, v in cdict.items() if v == g]
            ax.scatter(
                scatter_x.iloc[ix[0]], scatter_y.iloc[ix[0]], label=key[0], alpha=0.3)
        ax.set_xlabel(f"Component {comp_cons}")
        ax.set_ylabel(f"Component {comp_cons+1}")
        ax.set_title(
            f"ACP with filter {filter} conserving {summary[comp_cons]} of the variance")
        ax.legend()
        plt.show()
        st.pyplot(fig)

    except:
        ('error')


col_contrib()
