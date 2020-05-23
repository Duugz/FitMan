import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime as dt

exerciseSummary_layout = html.Div([
    
    html.Div(id='exerciseSummary-display-value'),
    html.Br(),
    dcc.Link('Create New Exercise', href='/createExercise'),
])

createExercise_layout = html.Div([
    html.H1("Create Exercise"),
    html.Br(),
    html.I("Select Exercise"),
    dcc.Dropdown(
        id='createExercise-dropdown',
        options=[
            {'label': 'Swim', 'value': 'Swim'},
            {'label': 'Run', 'value': 'Run'},
            {'label': 'Soccer', 'value': 'Soccer'},
            {'label': 'Boxing', 'value': 'Boxing'},
            {'label': 'Tennis', 'value': 'Tennis'},
            {'label': 'Basketball', 'value': 'Basketball'},
            {'label': 'Paddle', 'value': 'Paddle'},
        ],
        value='Swim'
    ),
    html.Br(),
    html.I("Select the Date"),
    html.Br(),
    dcc.DatePickerSingle(
        id='createExercise-date-picker',
        min_date_allowed=dt(2020, 5, 23),
        max_date_allowed=dt(2024, 9, 19),
        initial_visible_month=dt(2020, 8, 5),
        date=str(dt(2020, 8, 25, 23, 59, 59))
    ),
    html.Br(),
    html.I("How long?"),
    dcc.Slider(
    id='createExercise_length_slider',
    min=0,
    max=240,
    step=None,
    marks={
        0: '0 M',
        5: '5 M',
        10: '10 M',
        15: '15 M',
        20: '20 M',
        25: '25 M',
        30: '30 M',
        45: '45 M',
        60: '60 M',
        90: '90 Mins',
        120: '2 Hours',
        150: '2.5 Hours',
        180: '3 Hours ',
        210: '3.5 Hours',
        240: '4 Hours',
        },
    value=5
    ),
    html.Br(),
    html.I("What intensity?"),
    dcc.Slider(
    id='createExercise_intensity_slider',
    min=0,
    max=10,
    step=None,
    marks={
        0: 'Easy',
        1: '1 '     ,
        2: '2 ',
        3: '3 ',
        4: '4',
        5: 'Medium',
        6: '6',
        7: '7',
        8: 'Hard',
        9: '9',
        10: 'ALL OUT',
        },
    value=5
    ),
    html.Div(id='createExercise-display-value'),
    html.Br(),
    html.A(
        html.Button('Submit'),
        href='/exerciseSummary'
    ),
    html.Br(),
    html.A(
        html.Button('Cancel'),
        href='/exerciseSummary',
    ),
])

start_layout = html.Div([
    html.Div(id ='start-display-value'),
    html.Br(),
    dcc.Link('Go to Exercise Summary', href='/exerciseSummary'),   
])
