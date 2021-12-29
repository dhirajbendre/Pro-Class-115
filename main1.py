import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

temperature_list  = df["Temperature"].tolist()
melted_list = df["Melted"].tolist()

fig = px.scatter(x=temperature_list, y=melted_list)
fig.show()

import numpy as np
temperature_array = np.array(temperature_list)
melted_array = np.array(melted_list)

m, c = np.polyfit(temperature_array, melted_array, 1)

y = []
for x in temperature_array:
    y_value = m*x + c
    y.append(y_value)

fig = px.scatter(x=temperature_array, y=melted_array)
fig.update_layout(shapes=[
    dict(
        type ='line',
        y0= min(y), y1= max(y),
        x0= min(temperature_array), x1= max(temperature_array),
    )

])    
fig.show()