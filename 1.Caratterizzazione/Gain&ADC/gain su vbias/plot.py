import pandas as pd
import plotly.express as px

file_path = "56.5v.CSV"  # Replace with your CSV file path
data = pd.read_csv(file_path, delimiter=';', skiprows=1, names=['Channel', 'Counts'])
fig = px.line(data, x='Channel', y='Counts')
fig.show()
