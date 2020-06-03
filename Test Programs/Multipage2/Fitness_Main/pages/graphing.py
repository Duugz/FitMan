import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output



graphing_layout = html.Div([
    dcc.Link('Back to Main Menu', href='/'),
    html.Br()
])
