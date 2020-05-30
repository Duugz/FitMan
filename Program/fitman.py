import dash

fitman = dash.Dash(__name__, suppress_callback_exceptions=True)

fitman.server.secret_key = "OCML3BRawWEUeaxcuKHLpw"

server = fitman.server
