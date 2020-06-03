import dash #framework 

fitman = dash.Dash(__name__, suppress_callback_exceptions=True)
fitman.server.secret_key = "OCML3BRawWEUeaxcuKHLpw"

server = fitman.server
#these three lines of code define fitman as the Dash app __name__
#supress the callback exceptions (not every button needs a callback decorator)
#and makes the server variable (see index) fitman.
