import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

index_layout = html.Div([
    html.I("Enter Username and Password"),
    html.Br(),
        dcc.Input(id="Username", type="text", placeholder=""),
        dcc.Input(id="Password", type="text", placeholder="", debounce=True),
    html.Div(id="output"),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic'),

    html.Div(id='content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
])
