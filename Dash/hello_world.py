from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import webbrowser
from threading import Timer

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

port = 5000 # or simply open on the default `8050` port

def open_browser():
	webbrowser.open_new("http://localhost:{}".format(port))

if __name__ == '__main__':
    Timer(1, open_browser).start();
    app.run_server(debug=True, port=port)