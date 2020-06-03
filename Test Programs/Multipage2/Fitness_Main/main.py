import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import graphing
from pages import index
from pages import details

app = dash.Dash()

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

#Homepage Callback
@app.callback(dash.dependencies.Output('homepage-content', 'children'),
              [dash.dependencies.Input('homepage-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)

#Details 
@app.callback(Output('page-2-content', 'children'),
              [Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)

#Graphing Page Callback
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return homepage.homepage_layout
    elif pathname == '/details':
        return details.details_layout
    elif pathname == '/graphing':
        return graphing.graphing_layout
    else:
        return '404'

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
