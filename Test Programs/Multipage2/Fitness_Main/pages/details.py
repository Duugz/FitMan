import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

details_layout = html.Div([
    html.H1('Details'),
    html.Div(id='details-content'),
    html.Br(),
    dcc.Link('Back to Menu', href='/page-1'),
    html.Br(),
])
