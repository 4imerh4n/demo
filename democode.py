import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {'Category': ['A', 'B', 'C', 'D', 'E'], 
        'Value': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Create a bar chart
fig, ax = plt.subplots()
ax.bar(df['Category'], df['Value'])

# Create a Streamlit app
st.title("Bar Chart Example")
st.write("This is a simple bar chart example on Streamlit.")
st.pyplot(fig)
