import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('Dubai.csv')
sns.set_theme(font = 'serif')
plt.figure(figsize=(8,7))
sns.heatmap(corr_matrix,annot=True,cmap='PuBuGn',linewidths=.5)
plt.title('Correlation Heatmap', fontdict={'fontweight': 'bold'}, fontsize=15, color='green',pad=10)
plt.show()
