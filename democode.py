import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('Dubai.csv')
sns.set(style="whitegrid")
sns.set_theme(font = 'serif')

pairplot = sns.pairplot(df, vars=['Rent', 'Beds', 'Baths', 'Area_in_m2', 'Rent_per_m2'],
                        hue='Rent_category',diag_kind="kde", markers="o",
                        height=3, aspect=1, kind="scatter",
                        palette="Set2")

plt.show()
plt.show()
