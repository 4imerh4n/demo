import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = {'Category': ['A', 'B', 'C', 'D', 'E'], 
        'Value': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)
fig, ax = plt.subplots()
ax.bar(df['Category'], df['Value'])
st.pyplot(fig)
