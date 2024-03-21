from dash import Dash, dcc, html, Input, Output
from threading import Timer
import webbrowser
import os

app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'

port = 8050 # or simply open on the default `8050` port
def open_browser():
	webbrowser.open_new("http://localhost:{}".format(port))
		
if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run_server(debug=True)