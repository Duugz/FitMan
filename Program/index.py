import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from fitman import fitman
from layouts import createExerciseSummary_layout, createExercise_layout, createExerciseSummaryGraph_layout, createHomepage_layout, createAccount_layout
import callbacks


appName = "Fitman"
appVersion = "1.4"
appAuthor = "R.Duggan"

fitman.layout = html.Div([
    dcc.Location(id='url', refresh=False),
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
        return 'Unknown URL'

fitman.css.append_css({ 'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    fitman.run_server(debug=True)
