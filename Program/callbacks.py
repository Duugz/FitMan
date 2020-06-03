#This page contains all decorator callbacks for the program
#All unexplaied imports/code have been explained already on layouts.py
#-----------------------------
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components
import re # regular expressions
import sqlite3
import pandas as pd
import constants
from dash.dependencies import Input, Output, State
from fitman import fitman
from datetime import datetime as dt
from flask import session
import constants
from layouts import createHomepage_layout #this needs this for the purpose of

#------------------------------------------------------
#common callback code
#@fitman.callback



#this function makes sure that a users details are correct and then is called into the function login()
def searchUserFromDatabase(findUser):
    #as explained in layouts, the connection is established and a query is made with the UserID in mind
    conn = sqlite3.connect("C:\\Users\\Duugz\\FitMan\\fitman.db")
    selectsql = "SELECT UserID, Password, Username FROM User WHERE Username = '" + findUser + "'"
    
    #print(selectsql) debugging print()
    dataframe = pd.read_sql_query(selectsql, conn)
    
    #see layouts for definition of to_dict
    valueList = dataframe.to_dict('records')
    #valueDict = valueList[1]
    #valueList = list(dataframe)
    #I didnt know which one would work a library or a list so here is some random list() code
    #print(valueList)

    
    for user in valueList:
    #if len(valueList) > 0:
        #selects whichever corrosponding value for each variable
        password = user.get("Password")
        username = user.get("Username")
        userID = user.get("UserID")

        user = (userID, username, password)
        #print(user)
        
        return user
    
    return 

#login callback
@fitman.callback(
    dash.dependencies.Output("login-output", "children"),
    [Input('login-button', 'n_clicks'),
     Input("username", "value"),
     Input("password", "value")
     ])
def login(n_clicks, username, password):  
    
    #print("login called " + str(n_clicks))
    if n_clicks > 0:
        #print("login and n_clicks " + username)
        #more debugging statements I used
        user = searchUserFromDatabase(username)
        
        #print(user)
        #if username is not found in the database it will return 
        if user is None:
            return "No such User"
        #username exists in database but password doesn't 
        elif user[2] != password:
            return "Password not found"
        else:      
            #keeps these two variables in the session to display on the page or to be used later (see below)
            session[constants.SESSION_USERNAME_FIELD] = user[1]
            session[constants.SESSION_USERID_FIELD] = user[0]

            return "Welcome back " + user[1] + "! Click Home to continue"
    else:
        return   
#logout callback
@fitman.callback(
    dash.dependencies.Output("logout-output", "children"),
    [Input('logout-button', 'n_clicks')
     ])
def logout(n_clicks):
    if n_clicks > 0:
        print("Logout Called")
        session.pop(constants.SESSION_USERNAME_FIELD)
        session.pop(constants.SESSION_USERID_FIELD)
        return
    else:
        return



#createUser callback
@fitman.callback(
    dash.dependencies.Output("createUser-output", "children"),
    [Input('submitUser-btn', 'n_clicks'),
     Input("newUser", "value"),
     Input("newPass", "value")
     ])
def addUserToDatabase(n_clicks, newUser, newPass):

    if n_clicks > 0:

        if searchUserFromDatabase(newUser) is not None:

            return "Sorry, that username already exists"

        else:
        
            connectionAdd = sqlite3.connect("C:\\Users\\Duugz\\FitMan\\fitman.db")
            cursor = connectionAdd.cursor()

            insertSQL = 'INSERT INTO User (Username, Password) VALUES ({},{})'
            insertSQL = insertSQL.format("'" + newUser + "'","'"+ newPass+"'")
            print(insertSQL)
            
            countAdd = cursor.execute(insertSQL)
            connectionAdd.commit()

            cursor.close()
            connectionAdd.close()
            return "Your account has been created! Click Back to login" 

    return



#createExercise page callbacks
@fitman.callback(
    dash.dependencies.Output('form-end', 'children'),
    [Input('submit-btn', 'n_clicks' )],
    [State('createExercise-exercise', 'value'),
     State('createExercise-date-picker', 'date'),
     State('createExercise-length-slider', 'value'),
     State('createExercise-intensity-slider', 'value')
    ])
#state refers to the state of the str and orders them   
def addExerciseToDatabase(n_clicks, exerciseValue, dateStr, lengthValue, intensityValue):

    if n_clicks > 0:

        connectionAdd = sqlite3.connect("C:\\Users\\Duugz\\FitMan\\fitman.db")
        cursor = connectionAdd.cursor()

        #not really sure why this works, but sometimes the date would appear with time. This stopped that.

        date = dt.strptime(re.split('T| ', dateStr)[0], '%Y-%m-%d')
        #try:
            
        userID = session[constants.SESSION_USERID_FIELD]

        #except:

            #return 'System Error, no userID found in session'
        
        insertSQL = 'INSERT INTO Exercises (UserID, ExerciseType, ExerciseDate, LengthMins, Intensity) VALUES ('+ str(userID) +',"{}","{}",{},{})'
        insertSQL = insertSQL.format(exerciseValue, date.strftime('%Y-%m-%d'), lengthValue, intensityValue)
        countAdd = cursor.execute(insertSQL)
        connectionAdd.commit()

        cursor.close()

        connectionAdd.close()
    
    
        return 'You have submitted "{}" on the "{}" for "{}" minutes at "{}" intensity'.format(exerciseValue, dateStr, lengthValue, intensityValue)
    else:
        return

#addExerciseToDatabase - gives the function within the createExercises page, starting data as a string, pulling it apart to be fed into .format which then
#reforms it into a string again. This is the only way to make the SQL data work with my dash (that i could find)
#return 'You\'ve entered "{}", "{}", "{}", "{}"'.format(exerciseValue, dateValue, lengthValue, intensityValue) gives the message after submitting
#%Y-%m-%d arranges date in years/months/days


#help screens callbacks

@fitman.callback(
      Output("login-help", "is_open"),
     [Input("login-open", "n_clicks"),
      Input("login-close", "n_clicks")],
      [State("login-help", "is_open")],
)
def show_help(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@fitman.callback(
     Output("main-menu-help", "is_open"),
    [Input("main-menu-open", "n_clicks"),
     Input("main-menu-close", "n_clicks")],
     [State("main-menu-help", "is_open")],
)
def show_help(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
    
@fitman.callback(
     Output("new-help", "is_open"),
    [Input("new-open", "n_clicks"),
     Input("new-close", "n_clicks")],
     [State("new-help", "is_open")],
)
def show_help(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@fitman.callback(
    Output("summary-help", "is_open"),
    [Input("summary-open", "n_clicks"),
     Input("summary-close", "n_clicks")],
    [State("summary-help", "is_open")],
)
def show_help(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
    
@fitman.callback(
    Output("graph-help", "is_open"),
    [Input("graph-open", "n_clicks"),
     Input("graph-close", "n_clicks")],
    [State("graph-help", "is_open")],
)
def show_help(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
    
@fitman.callback(
    Output("createExercise-help", "is_open"),
    [Input("createExercise-open", "n_clicks"),
     Input("createExercise-close", "n_clicks")],
    [State("createExercise-help", "is_open")],
)
def show_help(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#this form of callback doesn't work for what i want to do because the program cant progress having multiple inputs, outputs and states all at one time.

##@fitman.callback(
##     [Output("login-help", "is_open"),
##     Output("main-menu-help", "is_open"),
##     Output("newUser-help", "is_open"),
##     Output("summary-help", "is_open"),
##     Output("graph-help", "is_open"),
##     Output("createExercise-help", "is_open")],
##    [Input("login-open", "n_clicks"), Input("login-close", "n_clicks"),
##    Input("main-menu-open", "n_clicks"), Input("main-menu-close", "n_clicks"),
##    Input("newUser-open", "n_clicks"), Input("newUser-close", "n_clicks"),
##    Input("summary-open", "n_clicks"), Input("summary-close", "n_clicks"),
##    Input("graph-open", "n_clicks"), Input("graph-close", "n_clicks"),
##    Input("createExercise-open", "n_clicks"), Input("createExercise-close", "n_clicks")
##     ],
##     [State("login-help", "is_open"),
##     State("main-menu-help", "is_open"),
##     State("newUser-help", "is_open"),
##     State("summary-help", "is_open"),
##     State("graph-help", "is_open"),
##     State("createExercise-help", "is_open")],
##)








    
    
