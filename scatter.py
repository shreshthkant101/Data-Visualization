import pandas as pd
import plotly.express as px

frame = pd.read_csv("data.csv")

graph = px.scatter(frame,x="Population",y="Per capita",size="Percentage",color="Country",size_max=60)

graph.show()