import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

homepage = dash.Dash(__name__, external_stylesheets=external_stylesheets)

homepage.layout = html.Div(
    [
        html.I("Enter Username and Password"),
        html.Br(),
        dcc.Input(id="Username", type="text", placeholder=""),
        dcc.Input(id="Password", type="text", placeholder="", debounce=True),
        html.Div(id="output"),
        html.Button('Submit', id='submit-val', n_clicks=0),
        html.Div(id='container-button-basic'),
    ]
)

@homepage.callback(
    Output("output", "children"),
    [Input("Username", "value"), Input("Password", "value")],
    
)


def update_output(input1, input2):
    return u'{} {}'.format(input1, input2)

#not useful yet
#def get_login(func):
#    def func_login():
#        if LOGGED_IN:
#            return func()
#        else:
#            html.Div([
#        html.H1('Incorrect')
#    ])
#            return homepage_page
#    return func_login
#
#@get_login
#def render_page():
#    return html.Div([
#        html.H1('Welcome')
#    ])


if __name__ == "__main__":
    homepage.run_server(debug=True)
#__main__ and __name__ correspond with each other. Whereas other langauges
# use main() python uses __name__ and __main__ as a way of defining special variables
 
