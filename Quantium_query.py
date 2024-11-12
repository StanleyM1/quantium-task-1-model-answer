from ast import main
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd 

# file_reader.py

class FileReader:

    def read_file(self):
        with open(self.quantium-task-1-model-answer-main, 'r') as file:
            content = file.read()
            return content

app = Dash(__name__)

app.title = "Quantium Task 1"


df = px.data.gapminder().query("Chart == 'Dates'")

fig = px.line(df, x="daily_sales_data_0", y="Year", title='Last Year Sales Data')

fig.show()