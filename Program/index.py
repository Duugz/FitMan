import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from fitman import fitman
from layouts import getExerciseSummary_layout, createExercise_layout, start_layout, exerciseSummaryGraph_layout
import callbacks

fitman.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='index')
])


#Index Page callback
@fitman.callback(Output('index', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return start_layout
    elif pathname == '/createExercise':
        return createExercise_layout
    elif pathname == '/exerciseSummary':
        return getExerciseSummary_layout()
    elif pathname == '/graph:
        return exerciseSummaryGraph_layout()
    else:
        return 'Unknown URL'

fitman.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    fitman.run_server(debug=True)
