import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import sqlite3
from dash.dependencies import Input, Output
from datetime import datetime as dt


#testExercise = {"Date": ["19/02/03", "19/02/03"],
     #"Intensity": ["Hard", "Hard"],
     #"Exercise": ["Soccer", "Soccer"],
     #"Length": ["1 Hour", "2 Hours"]}


def getExercisefromdatabase():

    conn = sqlite3.connect("C:\\Users\\Duugz\\FitMan\\fitman.db") 
    df = pd.read_sql_query("SELECT ExerciseDate, ExerciseType, Intensity, LengthMins FROM Exercises WHERE UserID = 5 ORDER by ExerciseDate DESC", conn)
    
    return df

def addExerciseToDatabase():

    #connector = sqlite3.connect("C:\\Users\\Duugz\\FitMan\\fitman.db")
    #dataframe = pd.read_sql_query(INSERT INTO Exercises (ExerciseID, ExerciseDate, ExerciseType, Intensity, LengthMins)
                                  #VALUES ()
    print('test')
    return 
      


def getExerciseSummary_layout():

    df = getExercisefromdatabase()#df stands for dataframe, that passes into the function

    return html.Div([
        html.H1("Exercise Summary"),
        html.Br(),
        html.I("Your Exercises"),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
        ),
        html.Div(id='exerciseSummary-display-value'),
        html.Br(),
        html.A(
            html.Button('Create New Exercise'),
            href='/createExercise',)
        ])
  
createExercise_layout = html.Div([
    html.H1("Create Exercise"),
    html.Br(),
    html.I("Select Exercise"),
    dcc.Dropdown(
        id='createExercise-exercise',
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
        min_date_allowed=dt(2018, 5, 23),
        max_date_allowed=dt(2024, 9, 19),
        initial_visible_month=dt(2020, 8, 5),
        date=str(dt(2020, 8, 25)),
        ),

    html.Br(),
    html.I("How long?"),
    dcc.Slider(
        id='createExercise-length-slider',
        min=0,
        max=240,
        step=None,
        marks={
        5: '5 M',
        10: '10 M',
        15: '15 M',
        20: '20 M',
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
    value=60
    ),
    
    html.Br(),
    html.I("What intensity?"),
    dcc.Slider(
        id='createExercise-intensity-slider',
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
    html.Br(),
    #html.A(
    
    html.Button(id='submit-btn', n_clicks=0, children='Submit'),

    #id='btn-save-new-exercise'),
        #href='/exerciseSummary'
          
    #),
    #html.div(id="debug-message-insert"),
    html.Div(id='form-end'),
    
    html.Br(),
    html.A(
        html.Button('Back'),
        href='/exerciseSummary',
    ),
])

start_layout = html.Div([
    #html.H4("username"),
    #dcc.Input(id="username", placeholder="enter username", type="text"),
    #html.H4("password"),
    #dcc.Input(id="password", placeholder="enter password", type="password"),
    #html.Button("add user", id="add-button"),
    #html.Hr(),
    #html.H3("users"),
    #html.Div(id="users"),

    html.Div(id ='start-display-value'),
    html.Br(),
    dcc.Link('Go to Exercise Summary', href='/exerciseSummary'),   
])
