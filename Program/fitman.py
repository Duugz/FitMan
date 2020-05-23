import dash

from datetime import datetime as dt

#external_spreadsheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

fitman = dash.Dash(__name__, suppress_callback_exceptions=True)
server = fitman.server
