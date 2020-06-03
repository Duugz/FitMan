#This is the index page where the admin user will run the program from
#The reason it does this is because it has everything called into one location ie
#layouts, callbacks, constants and fitman
#for explainations on imports look at layouts.py

#__name__ - the name of module that is being run 
#__main__ - you can change __name__ if the module being run is imported (for example fitman). This is defined with Dash.dash(__main__) in fitman.py

#both of these are special variables in python^^

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from fitman import fitman
from layouts import createExerciseSummary_layout, createExercise_layout, createExerciseSummaryGraph_layout, createHomepage_layout, createAccount_layout
#calls all the layouts with specifics
import callbacks


#appName = "Fitman"
#appVersion = "1.4"
#appAuthor = "R.Duggan"
#debugging data^^^


#this layout will give each other layout an individual url 
fitman.layout = html.Div([
    dcc.Location(id='url', refresh=False),#dcc.location is for when a user enters a url after the dash port :8050
    html.Div(id='index')
])


#These urls will bring the logged in user to the given pathname, including any other url bringing you to a error page
@fitman.callback(Output('index', 'children'),
              [Input('url', 'pathname')])
def fitmanPaths(pathname):
    if pathname == '/':
        return createHomepage_layout()
    elif pathname == '/createAccount':
        return createAccount_layout()
    elif pathname == '/createExercise':
        return createExercise_layout()
    elif pathname == '/exerciseSummary':
        return createExerciseSummary_layout()
    elif pathname == '/graph':
        return createExerciseSummaryGraph_layout()
    else:
        return 'Unknown URL' #any other url it will return this

fitman.css.append_css({ 'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

#this will import the css that you have import wether it be a url or a text file
if __name__ == '__main__':
    fitman.run_server(debug=True, host = '0.0.0.0')
#if fitman is = server (which it is) than the server will run with debugging tools on
    
