import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

page_2_layout = html.Div([
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])
