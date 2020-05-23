import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

index_layout = html.Div([
    (id='content'),
    html.Br(),
    dcc.Link('Go to Exercise Summary', href='/exerciseSummary'),   
])
