import dash_core_components as dcc #the core componets library, used multiple times with buttons drop downs etc
import dash_html_components as html #every bit of text, field or graphing uses html. For example html.Div, html.Br etc
import dash_bootstrap_components as dbc #used for help menus, allow for a popup that can be exited
import dash_table #part of dash components, except it needs its own import due to it not being the core components library
import sqlite3# built into python, creates a connection between files for pandas to then run a query or insert
import pandas as pd #uses queries and inserts to use SQL code. SQLite uses SQL.
import plotly.graph_objs as go #imports graphing tech that i need
import constants #imports constants that are then added to a session
from flask import session #sessions make it so you can create constants for each page. ie isUserLoggedIn
from dash.dependencies import Input, Output
from datetime import datetime as dt #can order dates in certain orders such as YY/MM/DD = %Y%m%d
from datetime import timedelta
from fitman import fitman #main program

def getLoggedInPageHeader(): #displays a header above the page using the session Username or getLoggedInUsername 

    return html.Div([
        html.H1("FitMan"),
        html.H3("User: " + getLoggedInUsername()),
        html.Hr()
        ])

#grabs the Username from the session. It does this by using the constant which is created whenever a user logs in.
def getLoggedInUsername(): 
    try: 
        return session[constants.SESSION_USERNAME_FIELD]
    except:
        return ""


def isUserLoggedIn(): #this function checks that a user is logged in. I also hadn't used flags at all before so i this function into one

    isLoggedIn = False
    
    if getLoggedInUsername() == "":#this makes it so that page headers are text not a random variable.
        isLoggedIn = False
    else:
        isLoggedIn = True

    return isLoggedIn


def createHomepage_layout():

    #testGetExerciseForRob() part of the driver debug device (see below and in doc)

    if isUserLoggedIn(): 
    
        return html.Div([
        getLoggedInPageHeader(),

        html.H1("Welcome Back!"),
        
        html.Div(),
        html.A(
            html.Button('See Exercise Summary'),
            href='/exerciseSummary'),
        html.Br(),
        html.A(
            html.Button('See Exercise Graph'),
            href='/graph'),
        html.Br(),
        html.A(
            html.Button('Create New Exercise'),
            href='/createExercise'),
        html.Br(),
        html.Br(),
        html.A(
            html.Button('Logout', id='logout-button', n_clicks=0),
            href='/'),
        html.Div(id="logout-output"),
        html.Br(),
        html.Br(),
        dbc.Button("?", id="main-menu-open"),
        dbc.Modal(
            [
            dbc.ModalHeader("Help"),
            dbc.ModalBody('''

Welcome to FitMan!
This app is a great way to store data from your exercises, or to view exercises you have already entered! :)
To begin, click ‘Create New Exercise’ to add an exercise to your table
If you already have exercises, you can either view them in a table by clicking ‘View Exercise Summary’ or in a graph by clicking ‘View Exercise Graph’.
If you want to Logout of Fitman, hit the logout button.
Have Fun! :D
                          '''),
            dbc.ModalFooter(
                dbc.Button("Close", id="main-menu-close", className="m1-auto")
            ),
        ],
        id="main-menu-help",
        size="lg",
    ),
])
    
    else:
        return html.Div([
        html.H1("Welcome to FitMan!"),
        html.Div(),
        html.Br(),
        html.I("Enter Username: "),
        dcc.Input(id="username", type="text", placeholder="", debounce=True),
        html.Br(),
        html.Br(),
        html.I("Enter Password:  "),
        dcc.Input(id="password", type="text", placeholder="", debounce=True),
        html.Div(id="login-output"),
        html.Br(),
        html.Br(),
        html.Button('Login', id='login-button', n_clicks=0),
        html.Br(),
        html.Br(),
        html.A(
            html.Button('Create Account'),
            href='/createAccount'),
        html.Br(),
        html.A(
            html.Button('Home'),
            href='/',),
        html.Br(),
        html.Br(),
        dbc.Button("?", id="login-open"),
            dbc.Modal(
                [
                    dbc.ModalHeader("Help"),
                    dbc.ModalBody('''

If you already have an account, type in username and password then hit submit.
Once you see the display message ‘Login Complete’ click the home button

If you don't already have an account then click create account.

                    '''),
                    dbc.ModalFooter(
                    dbc.Button("Close", id="login-close", className="m1-auto")
                    ),
                ],
                id="login-help",
                size="lg",
            ),
        ])
        
        
        
        
        
        
def createAccount_layout():
    
    return html.Div([

    html.H1("Create New Account"),
    html.Div(id ='createAccount-'),
    html.I("Enter New Username and Password"),
    html.Br(),
    dcc.Input(id="newUser", type="text", placeholder="", debounce=True),
    dcc.Input(id="newPass", type="text", placeholder="", debounce=True),
    html.Div(id="createUser-output"),
    html.Br(),
    html.Button('Submit', id='submitUser-btn', n_clicks=0),
    html.Br(),
    html.Br(),
    html.A(
        html.Button('Back'),
        href='/',),
    html.Br(),
    html.Br(),
    dbc.Button("?", id="new-open"),
        dbc.Modal(
            [
                dbc.ModalHeader("Help"),
                dbc.ModalBody('''

Enter a new username and password into the respective boxes.
If anything other than ‘account created’ appears below it means you have entered a username or password that already exists

Hit back to return to the Login page

                '''),
                dbc.ModalFooter(
                dbc.Button("Close", id="new-close", className="ml-auto")
                ),
            ],
            id="new-help",
            size="lg",
        ),
])
    




#testExercise = {"Date": ["19/02/03", "19/02/03"],
     #"Intensity": ["Hard", "Hard"],
     #"Exercise": ["Soccer", "Soccer"],
     #"Length": ["1 Hour", "2 Hours"]}

#^^Used as a makeshift datatable before figuring out how to do query

#Driver Example
#def testGetExerciseForRob():
    #df = getExercisefromdatabase(5)
    #print("Robs Exercise Dataframe:" + str(df))



def getExercisefromdatabase(userID):

    conn = sqlite3.connect("C:\\Users\\Duugz\\FitMan\\fitman.db")
    df = pd.read_sql_query("SELECT ExerciseDate, ExerciseType, Intensity, LengthMins FROM Exercises WHERE UserID = " + str(userID) + " ORDER by ExerciseDate DESC", conn)
    
    return df

#def addExerciseToDatabase():

    #connector = sqlite3.connect("C:\\Users\\Duugz\\FitMan\\fitman.db")
    #dataframe = pd.read_sql_query(INSERT INTO Exercises (ExerciseID, ExerciseDate, ExerciseType, Intensity, LengthMins)
                                  #VALUES ()
    #print('test')
    #return
#early version of the queries that i use in actual program.
      


def createExerciseSummary_layout():

    df = getExercisefromdatabase(session[constants.SESSION_USERID_FIELD])#df stands for dataframe, that passes back from the function

    return html.Div([
        getLoggedInPageHeader(),
        html.Br(),
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
            href='/createExercise',),
        
        html.Br(),
        html.Br(),
        html.A(
            html.Button('View Progress Graph'),
            href='/graph',),
        
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        html.A(
        html.Button('Main Menu'),
        href='/',),
        html.Br(),
        dbc.Button("?", id="summary-open"),
            dbc.Modal(
                [
                    dbc.ModalHeader("Help"),
                    dbc.ModalBody('''

This is your Exercise Summary page.

You can add Exercises from here, or you can view your graph by clicking the respective buttons for each.

Click back to return to the main menu.

                    '''),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="summary-close", className="ml-auto")
                    ),
                ],
                id="summary-help",
                size="lg",
            ),
        
        ])
  
def createExercise_layout():

    return html.Div([
    getLoggedInPageHeader(),
    html.Br(),
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
    html.Button(id='submit-btn', n_clicks=0, children='Submit'),
    
    html.Div(id='form-end'),
    
    html.Br(),
    html.A(
        html.Button('View Summary'),
        href='/exerciseSummary',
    ),
    html.Br(),
    html.Br(),
    dbc.Button("?", id="createExercise-open"),
        dbc.Modal(
            [
                dbc.ModalHeader("Help"),
                dbc.ModalBody('''

Here is where all exercises are created :)

You can use the two dropdowns to set the data and sport that you did on the given day. 
Creating an exercise also involves using the two sliders to input the length and intensity of your workout.

Once you have entered all the fields to your desired time, click ‘Submit’. You should get a message saying ‘You have Submitted’ followed by your fields.
When this message appears, you can then hit ‘View Summary’ to return to the ‘Exercise Summary’ Page

                '''),
                dbc.ModalFooter(
                    dbc.Button("Close", id="createExercise-close", className="ml-auto")
                ),
            ],
            id="createExercise-help",
        ),
])



def getDatesandLengthsfromdatabase(userID):

    conn = sqlite3.connect("C:\\Users\\Duugz\\FitMan\\fitman.db") 
    df = pd.read_sql_query("SELECT ExerciseDate, LengthMins FROM Exercises WHERE UserID = " + str(userID) + " ORDER by ExerciseDate DESC", conn)      
    return df
    
    
def createExerciseSummaryGraph_layout():

    df = getDatesandLengthsfromdatabase(session[constants.SESSION_USERID_FIELD])
    databaseDict = df.to_dict('records')

    #create a dictionary with an entry for every date that =0
    graphDict = dict()

    startDate = dt.strptime("2020-08-01", "%Y-%m-%d")  
    endDate = dt.strptime("2020-11-01", "%Y-%m-%d")  

    dayCount = (endDate - startDate).days + 1
    for singleDate in (startDate + timedelta(n) for n in range(dayCount)):
        graphDict[singleDate]=0    
    
    
    #for every date in the database, add the length to the value in the dictionary
    for exer in databaseDict:

        eDate= dt.strptime(exer.get("ExerciseDate"), "%Y-%m-%d")    
        lengthMins = int(exer.get("LengthMins"))

        dayLengthMins = graphDict.get(eDate)
        graphDict[eDate]= dayLengthMins + lengthMins


    #build an aray of x and v values for the graph
    eDateArr = []
    eLengthArr = []

    for singleDate in (startDate + timedelta(n) for n in range(dayCount)):

        dayLengthMins = graphDict[singleDate]
        eDateArr = eDateArr + [singleDate]
        eLengthArr = eLengthArr + [dayLengthMins]

    fig=go.Figure(
        data=[go.Bar(
                      x=eDateArr,
                      y=eLengthArr)
               ])
        #The graphshows down the bottom, dates from the first workout to the last recorded and calculates dates inbetween. Unforutnetly I could not find a way to control this properly

    return  html.Div([
        getLoggedInPageHeader(),
        html.Br(),
        dcc.Graph(
            id='exerciseSummaryGraph',
            figure=fig     
        ),
        html.Br(),
        html.A(
            html.Button('View Exercise Summary'),
            href='/exerciseSummary'),
        html.Br(),
        html.A(
            html.Button('Create New Exercise'),
            href='/createExercise'),
        html.Br(),
        html.A(
            html.Button('Main Menu'),
            href='/'),
        html.Br(),
        html.Br(),
        dbc.Button("?", id="graph-open"),
            dbc.Modal(
                [
                    dbc.ModalHeader("Help"),
                    dbc.ModalBody('''

You can hover over each bar in the graph to display the date that it occurred on. 
Also using the dash tools in the top right of the graph you can zoom in and out as well as other devices.

Try it!

Use the ‘Create New Exercise’ to add an exercise to your table from here
You can view exercises in table form by clicking ‘View Exercise Summary’ 
Return to Main Menu with the respective buttons.

                    '''),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="graph-close", className="ml-auto")
                    ),
                ],
                id="graph-help",
            ),
    ])








