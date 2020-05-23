import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

exerciseSummary_layout = html.Div([
    html.Div(id='exerciseSummary-display-value'),
    html.Br(),
    dcc.Link('Create New Exercise', href='/createExercise'),
])

createExercise_layout = html.Div([
    html.Div(id='createExercise-display-value'),
    html.Br(),
    dcc.Link('Cancel', href='/exerciseSummary'),
    html.Br(),
    dcc.Link('Submit', href='/exerciseSummary')
])

index_layout = html.Div([
    html.Div(id ='index-display-value'),
    html.Br(),
    dcc.Link('Go to Exercise Summary', href='/exerciseSummary'),   
])
