import pandas as pd
import plotly.express as px

frame = pd.read_csv("data.csv")

graph = px.bar(frame,x="Country",y="InternetUsers")

graph.show()