import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from datetime import datetime 
from fitman import fitman

#createExercise page callbacks
@fitman.callback(
    dash.dependencies.Output('createExercise-exercise', 'children'),
    [dash.dependencies.Input('createExercise-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

@fitman.callback(
    Output('createExercise-date', 'children'),
    [Input('createExercise-date-picker', 'date')])
def display_value(date):
    string_prefix = 'You have selected: '
    if date is not None:
        date = dt.strptime(re.split('T| ', date)[0], '%Y-%m-%d')
        date_string = date.strftime('%B %d, %Y')
        return string_prefix + date_string

@fitman.callback(
    dash.dependencies.Output('createExercise-length', 'children'),
    [dash.dependencies.Input('createExercise-length-slider', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
@fitman.callback(
    dash.dependencies.Output('createExercise-display-value', 'children'),
    [dash.dependencies.Input('createExercise-intensity-slider', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

