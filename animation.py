
#import the necessary modules
from dash import Dash, dcc, html, callback, Output, Input
import pandas as pd
import plotly.express as px

#connect to the data
#df=pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
df=px.data.gapminder()
#initialise the app
app=Dash(__name__)
colors={
    'background':'#111111',
    'text':'#7FDBFF'
}
#define app layout
app.layout=html.Div(style={'backgroundColor':colors['background']}, children=[
    html.H1(children='Animated GDP and population over the decades', style={'color':'red','textAlign':'center','fontSize':'50px'}),
    html.P('Select an animation', style={'color':colors['text']}),
    dcc.RadioItems(options=[
        {'label':'GDP Per Capita', 'value':'gdpPercap'},
        {'label':'Population','value':'pop'}],
        value='gdpPercap',
        id='buttons',
        style={'color':colors['text']}
    ),
    dcc.Loading(dcc.Graph(id='graph', style={'backgroundColor':colors['background']}), type='cube')
])

#callback decorator to connect between the graph and radio items
@callback(
    Output('graph','figure'),
    Input('buttons','value')
)
def dataApp(buttons):
    animations={
        'gdpPercap':px.scatter(
            df, x='gdpPercap',
            y='lifeExp',
            animation_frame='year',
            animation_group='country',
            size='pop',
            color='continent',
            hover_name='country',
            log_x=True,
            size_max=55,
            range_x=[100,100000],
            range_y=[25,90]
        ),
        'pop':px.bar(
            df, x='continent',
            y='pop',
            color='continent',
            animation_frame='year',
            animation_group='country',
            range_y=[0,4000000000]
        )
    }
    return animations[buttons]

#run the app
if __name__ == '__main__':
    app.run(debug=True)
