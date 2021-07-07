import pandas as pd
import plotly.express as px


frame = pd.read_csv("line_chart.csv")


fig = px.line(frame,x="Year",y="Per capita income",color="Country",title="Per capita income")

fig.show()

