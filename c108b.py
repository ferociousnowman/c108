import pandas as pd 
import csv
import plotly.figure_factory as ff

df=pd.read_csv('data.csv')
HeightList=df['Height(Inches)'].tolist()
fig=ff.create_distplot([HeightList],['Height'])
fig.show()