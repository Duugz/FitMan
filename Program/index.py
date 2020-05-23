import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime as dt
from fitman import fitman
from layouts import getExerciseSummary_layout, createExercise_layout, start_layout

fitman.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


#Index Page callback
@fitman.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return start_layout
    elif pathname == '/createExercise':
        return createExercise_layout
    elif pathname == '/exerciseSummary':
        return getExerciseSummary_layout()
    else:
        return '404'

fitman.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    fitman.run_server(debug=True)
