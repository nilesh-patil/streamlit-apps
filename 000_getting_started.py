import numpy as np 
import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')

st.write("##### Import packages :")

code_packages = """
import numpy as np 
import pandas as pd
import streamlit as st
"""
st.code(code_packages, language='python')

st.write("##### Create Sample Data : ")


n_centers  = st.sidebar.number_input(label="Provide Number of clusters :", min_value=1, max_value= 100, step=1, value=25)
n_features = st.sidebar.number_input(label="Provide Number of features :", min_value=1, max_value= 25, step=1, value=5)
n_centers = int(n_centers)
n_features = int(n_features)

centers = np.random.randint(low=-10, high=10, size=(n_centers, n_features))
centers_df = pd.DataFrame(data=centers, columns=[f"col_{i}" for i in range(n_features)] )

code_data_generate = """
n_centers  = int(st.sidebar.number_input(label="Provide Number of clusters :", min_value=1, max_value= 100, step=1, value=10))
n_features = int(st.sidebar.number_input(label="Provide Number of features :", min_value=1, max_value= 25, step=1, value=5))


centers = np.random.randint(low=-10, high=10, size=(n_centers, n_features))
centers_df = pd.DataFrame(data=centers, columns=[f"col_{i}" for i in range(n_features)], index=[f"center_{i}" for i in range(n_centers)] )
"""

st.code(code_data_generate, language='python')


st.write("##### Show Sample Data : ")

code_data_write_01 = """
st.code(code_data_write_01, language='python')
st.dataframe(data=centers_df.head(5), width=950)
"""
st.code(code_data_write_01, language='python')
st.dataframe(data=centers_df.head(5), width=950)


st.write("##### Create Walks : ")

code_data_write_02 = """
x = np.arange(start=1, stop=n_centers)
data = centers_df.cumsum(axis=0)
st.dataframe(data=data.head(5), width=950)
"""
st.code(code_data_write_02, language='python')


x = np.arange(start=1, stop=n_centers)
data = centers_df.cumsum(axis=0)
st.dataframe(data=data.head(5), width=950)

st.write("#### Plot Walks : ")


code_plot = """
st.dataframe(data=data.head(5), width=950)
st.line_chart(data)
"""
st.code(code_data_write_02, language='python')

st.line_chart(data)

