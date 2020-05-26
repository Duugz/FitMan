import dash
import dash_html_components as html
import dash_core_components as dcc
import re
import sqlite3
from dash.dependencies import Input, Output, State
from datetime import datetime 
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
    

def addExerciseToDatabase(n_clicks, exerciseValue, dateValue, lengthValue, intensityValue):

    if n_clicks > 0:

        connectionAdd = sqlite3.connect("C:\\Users\\Duugz\\FitMan\\fitman.db")
    

        cursor = connectionAdd.cursor()
        insertSQL = 'INSERT INTO Exercises (UserID, ExerciseType, ExerciseDate, LengthMins, Intensity) VALUES (5,"{}","{}",{},{})'
        insertSQL = insertSQL.format(exerciseValue, dateValue, lengthValue, intensityValue)
        countAdd = cursor.execute(insertSQL)
        connectionAdd.commit()

        cursor.close()

        connectionAdd.close()
    
    
        return 'You have submitted "{}" on the "{}" for "{}" minutes at "{}" intensity'.format(exerciseValue, dateValue, lengthValue, intensityValue)
    else:
        return  

     



#debug-message-insert
#addExerciseToDatabase
#return 'You\'ve entered "{}", "{}", "{}", "{}"'.format(exerciseValue, dateValue, lengthValue, intensityValue)

#%Y-%m-%d
