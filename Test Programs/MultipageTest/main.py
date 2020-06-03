import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from Pages import index
from Pages import page_1
from Pages import page_2

app = dash.Dash()

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='content')
])

# Page 1 callback
@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)

# Page 2
@app.callback(Output('page-2-content', 'children'),
              [Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)

# Index Page callback
@app.callback(Output('content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1.page_1_layout
    elif pathname == '/page-2':
        return page_2.page_2_layout
    elif pathname == '/':
        return index.index_layout
    else:
        return '404'

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
