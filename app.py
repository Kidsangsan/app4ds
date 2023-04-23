import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.header('st.button')
if st.button('Say hello'):
  st.write('Why hello there')
else:
  st.write('Goodbye')

df = pd.DataFrame({
     'first column':[1,2,3,4],
     'second column': [10,20,30,40]
    })
st.write(df)

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
