import dash
import dash_html_components as html
import dash_core_components as dcc
import re 
import sqlite3
from dash.dependencies import Input, Output, State
from fitman import fitman
from datetime import datetime as dt



#createExercise page callbacks
@fitman.callback(
    dash.dependencies.Output('form-end', 'children'),
    [Input('submit-btn', 'n_clicks' )],
    [State('createExercise-exercise', 'value'),
     State('createExercise-date-picker', 'date'),
     State('createExercise-length-slider', 'value'),
     State('createExercise-intensity-slider', 'value'),
     
    ])
#state refers to the state of the str and orders them   

def addExerciseToDatabase(n_clicks, exerciseValue, dateStr, lengthValue, intensityValue):

    if n_clicks > 0:

        connectionAdd = sqlite3.connect("C:\\Users\\Duugz\\FitMan\\fitman.db")
        cursor = connectionAdd.cursor()

        #not really sure why this works, but sometimes the date would appear with time. This stopped that.

        date = dt.strptime(re.split('T| ', dateStr)[0], '%Y-%m-%d')

        insertSQL = 'INSERT INTO Exercises (UserID, ExerciseType, ExerciseDate, LengthMins, Intensity) VALUES (5,"{}","{}",{},{})'
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
