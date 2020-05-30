import dash
import dash_html_components as html
import dash_core_components as dcc
import re 
import sqlite3
import pandas as pd
from dash.dependencies import Input, Output, State
from fitman import fitman
from datetime import datetime as dt
from flask import render_template, request, session, redirect, url_for
import constants
from layouts import createHomepage_layout



def searchUserFromDatabase(findUser):   
    conn = sqlite3.connect("C:\\Users\\Duugz\\FitMan\\fitman.db")
    selectsql = "SELECT UserID, Password, Username FROM User WHERE Username = '" + findUser + "'"
    print(selectsql)
    dataframe = pd.read_sql_query(selectsql, conn)

    valueList = dataframe.to_dict('records')
    #valueDict = valueList[1]
    #valueList = list(dataframe)
    print(valueList)
    for user in valueList:
    #if len(valueList) > 0:
        
        password = user.get("Password")
        username = user.get("Username")
        userID = user.get("UserID")

        user = (userID, username, password)
        print(user)
        
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
    
    print("login called " + str(n_clicks))
    if n_clicks > 0:
        print("login and n_clicks " + username)
        user = searchUserFromDatabase(username)
        
        #print(user)
        #if username is not found in the database it will return 
        if user is None:
            return "No such User"
        #username exists in database but password doesn't 
        elif user[2] != password:
            return "Password not found"
        else:      

            session[constants.SESSION_USERNAME_FIELD] = user[1]
            session[constants.SESSION_USERID_FIELD] = user[0]

            return "Welcome back " + user[1] + "! Click Home to see the main menu."
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
#@fitman.callback(


     


#addExerciseToDatabase - gives the function within the createExercises page, starting data as a string, pulling it apart to be fed into .format which then
#reforms it into a string again. This is the only way to make the SQL data work with my dash (that i could find)
#return 'You\'ve entered "{}", "{}", "{}", "{}"'.format(exerciseValue, dateValue, lengthValue, intensityValue) gives the message after submitting
#%Y-%m-%d arranges date in years/months/days
